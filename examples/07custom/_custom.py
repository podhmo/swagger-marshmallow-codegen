import bson
from swagger_marshmallow_codegen.driver import Driver
from swagger_marshmallow_codegen.dispatcher import TYPE_MAP, Pair, FormatDispatcher, ReprWrapString


class MyDispatcher(FormatDispatcher):
    type_map = {
        Pair(type="string", format="objectId"): "myschema:ObjectId",
        **TYPE_MAP,
    }

    def dispatch_default(self, c, value, field):
        if isinstance(value, bson.ObjectId) or field.get("format") == "objectId":
            c.import_("bson")
            return ReprWrapString("bson.{!r}".format(bson.ObjectId(value)))
        return super().dispatch_default(c, value, field)


class MyDriver(Driver):
    codegen_factory = Driver.codegen_factory.override(schema_class_path="myschema:MySchema")
    dispatcher_factory = MyDispatcher
