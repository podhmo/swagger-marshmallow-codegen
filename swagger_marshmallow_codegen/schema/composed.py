from collections import namedtuple, OrderedDict
from marshmallow import Schema, ValidationError, SchemaOpts
from marshmallow import marshalling
from prestring.utils import reify

StrategyContext = namedtuple("StrategyContext", "data, schemas, results, errors, compacted")


class ComposedOpts(SchemaOpts):
    def __init__(self, meta, **kwargs):
        super().__init__(meta, **kwargs)

        self.schema_classes = getattr(meta, "schema_classes", ())
        if not isinstance(self.schema_classes, (tuple, list)):
            raise ValueError("`schema_classes` must be a list or tuple.")

        self.discriminator = getattr(meta, "discriminator", None)
        if self.discriminator is not None:
            if "fieldname" not in self.discriminator:
                raise ValueError("`discriminator` must need `fieldname` value")


class OneOfSchema(Schema):
    OPTIONS_CLASS = ComposedOpts
    schema_classes = None

    def __init__(self, *args, **kwargs):
        strict = kwargs.pop("strict", None)
        many = kwargs.pop("many", None)
        schema_classes = self.opts.schema_classes or self.__class__.schema_classes
        self.schemas = [cls(*args, strict=False, many=False, **kwargs) for cls in schema_classes]
        super().__init__(strict=strict, many=many)

        finder = SchemaFinder(self.schemas, self.opts.discriminator)
        self._marshal = ComposedMarshaller(self._marshal, finder, self.final_check)
        self._unmarshal = ComposedUnmarshaller(self._unmarshal, finder, self.final_check)

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
    OPTIONS_CLASS = ComposedOpts
    schema_classes = None

    def __init__(self, *args, **kwargs):
        strict = kwargs.pop("strict", None)
        many = kwargs.pop("many", None)
        schema_classes = self.opts.schema_classes or self.__class__.schema_classes
        self.schemas = [cls(*args, strict=False, many=False, **kwargs) for cls in schema_classes]
        super().__init__(strict=strict, many=many)

        finder = SchemaFinder(self.schemas, self.opts.discriminator)
        self._marshal = ComposedMarshaller(self._marshal, finder, self.final_check)
        self._unmarshal = ComposedUnmarshaller(self._unmarshal, finder, self.final_check)

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


class SchemaFinder:
    def __init__(self, schemas, discriminator):
        self.schemas = schemas
        if discriminator is None:
            self.discriminator_name = None
            self.discriminator_mapping = None
        else:
            self.discriminator_name = discriminator["fieldname"]
            if "mapping" not in discriminator:
                self.discriminator_mapping = {s.__class__.__name__: s for s in schemas}
            else:
                mapping = {s.__class__: s for s in schemas}
                self.discriminator_mapping = {
                    name: mapping[cls]
                    for name, cls in discriminator["mapping"].items()
                }

    @reify
    def signature_mapping(self):
        d = OrderedDict()
        for s in self.schemas:
            sig = tuple(sorted([name for name, f in s.fields.items() if f.required]))
            d[sig] = s
        return d

    def find_matched_schemas(self, data):
        if self.discriminator_name is not None:
            return (self.discriminator_mapping[data[self.discriminator_name]], )

        r = []
        for signature, s in self.signature_mapping.items():
            if all(k in data for k in signature):
                r.append(s)
        return r

    def find_schemas(self, data):
        if self.discriminator_name is not None:
            return (self.discriminator_mapping[data[self.discriminator_name]], )
        return self.schemas


class ComposedMarshaller(marshalling.Marshaller):
    def __init__(self, marshaller, finder, final_check):
        super().__init__()
        self._marshaller = marshaller
        self.finder = finder
        self.final_check = final_check

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
        schemas = self.finder.find_matched_schemas(data)
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
    def __init__(self, unmarshaller, finder, final_check):
        super().__init__()
        self._unmarshaller = unmarshaller
        self.finder = finder
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
        schemas = self.finder.find_schemas(data)
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
