from collections import namedtuple
from marshmallow import Schema, ValidationError
from marshmallow import marshalling
from prestring.utils import reify

StrategyContext = namedtuple("StrategyContext", "data, schemas, results, errors, compacted")


class OneOfSchema(Schema):
    schema_clsses = None

    def __init__(self, *args, **kwargs):
        strict = kwargs.pop("strict", None)
        many = kwargs.pop("many", None)
        self.schemas = [
            cls(*args, strict=False, many=False, **kwargs) for cls in self.schema_classes
        ]
        super().__init__(strict=strict, many=many)

        self._marshal = ComposedMarshaller(self._marshal, self.schemas, self.final_check)
        self._unmarshal = ComposedUnmarshaller(self._unmarshal, self.schemas, self.final_check)

    def final_check(self, sctx):
        compacted = sctx.compacted
        if len(compacted) == 1:
            return compacted[0], {}
        elif len(compacted) > 1:
            for other in compacted[1:]:
                compacted[0].update(other)

            satisfied = []
            for i, err in enumerate(sctx.errors):
                if not err:
                    satisfied.append(sctx.schemas[i].__class__.__name__)
            return compacted[0], {
                "_schema": ["satisfied both of {}, not only one".format(satisfied)]
            }
        else:
            results = sctx.results
            for other in results[1:]:
                results[0].update(other)
            return sctx.data if not results else results[0], {
                "_schema":
                ["not matched, any of {}".format([s.__class__.__name__ for s in self.schemas])]
            }


class AnyOfSchema(Schema):
    schema_clsses = None

    def __init__(self, *args, **kwargs):
        strict = kwargs.pop("strict", None)
        many = kwargs.pop("many", None)
        self.schemas = [
            cls(*args, strict=False, many=False, **kwargs) for cls in self.schema_classes
        ]
        super().__init__(strict=strict, many=many)

        self._marshal = ComposedMarshaller(self._marshal, self.schemas, self.final_check)
        self._unmarshal = ComposedUnmarshaller(self._unmarshal, self.schemas, self.final_check)

    def final_check(self, sctx):
        compacted = sctx.compacted
        if len(compacted) >= 1:
            for other in compacted[1:]:
                compacted[0].update(other)
            return compacted[0], {}
        else:
            results = sctx.results
            for other in results[1:]:
                results[0].update(other)
            return sctx.data if not results else results[0], {
                "_schema":
                ["not matched, any of {}".format([s.__class__.__name__ for s in self.schemas])]
            }


def run_many(data, fn, **kwargs):
    results = []
    errors = {}
    for i, d in enumerate(data):
        r, err = fn(d, **kwargs)
        results.append(r)
        if err:
            errors[i] = err
    return results, errors


class ComposedMarshaller(marshalling.Marshaller):
    def __init__(self, marshaller, schemas, final_check):
        super().__init__()
        self._marshaller = marshaller
        self.schemas = schemas
        self.final_check = final_check

    @reify
    def mapping(self):
        d = {}
        for s in self.schemas:
            sig = tuple(sorted([name for name, f in s.fields.items() if f.required]))
            d[sig] = s
        return d

    def find_matched_schemas(self, data):
        r = []
        for signature, s in self.mapping.items():
            if all(k in data for k in signature):
                r.append(s)
        return r

    def marshall(self, obj, fields_dict, *, many, accessor, dict_class, index_errors, index=None):
        self.reset_errors()
        self_errors = None
        try:
            result = self._marshaller(
                obj,
                fields_dict,
                many=many,
                accessor=accessor,
                dict_class=dict_class,
                index_errors=index_errors,
                index=index,
            )
        except ValidationError as err:
            self_errors = self._marshal.errors
            result = err.data

        if many:
            d, errors = run_many(obj, self._marshall_one)
            for i in range(len(result)):
                d[i].update(result[i])
        else:
            d, errors = self._marshall_one(obj)
            d.update(result)
        if self_errors is not None:
            errors.update(self_errors)
        self.errors = errors
        if errors:
            raise ValidationError(errors, data=d)
        return d

    __call__ = marshall

    def _marshall_one(self, data):
        results = []
        errors = []
        compacted = []
        schemas = self.find_matched_schemas(data)
        for s in schemas:
            r, err = s.dump(data, update_fields=False)
            if not err:
                compacted.append(r)
            results.append(r)
            errors.append(err)
        sctx = StrategyContext(
            data=data, results=results, errors=errors, schemas=schemas, compacted=compacted
        )
        return self.final_check(sctx)


class ComposedUnmarshaller(marshalling.Unmarshaller):
    def __init__(self, unmarshaller, schemas, final_check):
        super().__init__()
        self._unmarshaller = unmarshaller
        self.schemas = schemas
        self.final_check = final_check

    def unmarshall(self, data, fields, *, many, partial, dict_class, index_errors):
        self.reset_errors()
        self_errors = None
        try:
            result = self._unmarshaller(
                data,
                fields,
                many=many,
                partial=partial,
                dict_class=dict_class,
                index_errors=index_errors,
            )
        except ValidationError as err:
            self_errors = self._unmarshaller.errors
            result = err.data

        if many:
            d, errors = run_many(data, self._unmarshall_one, partial=partial)
            for i in range(len(result)):
                d[i].update(result[i])
        else:
            d, errors = self._unmarshall_one(data, partial=partial)
            d.update(result)
        if self_errors is not None:
            errors.update(self_errors)
        self.errors = errors
        return d

    __call__ = unmarshall

    def _unmarshall_one(self, data, *, partial):
        results = []
        errors = []
        compacted = []
        schemas = self.schemas
        for s in schemas:
            r, err = s.load(data, partial=partial)
            if not err:
                compacted.append(r)
            results.append(r)
            errors.append(err)
        sctx = StrategyContext(
            data=data, results=results, errors=errors, schemas=schemas, compacted=compacted
        )
        return self.final_check(sctx)
