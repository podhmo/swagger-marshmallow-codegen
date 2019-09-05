# -*- coding:utf-8 -*-
import logging
from marshmallow.decorators import tag_processor


logger = logging.getLogger(__name__)


def xxx_modify_field(schema_cls, name):
    def action(modify):
        logger.debug("\t xxx: modify field=%r schema=%r, ", name, schema_cls)
        fields = schema_cls._declared_fields
        modify(fields[name])
        return modify

    return action


def xxx_add_processor(cls, tag, pass_many=False, pass_original=False):
    logger.debug("\t xxx: add tag=%r, pass_many=%r", tag, pass_many)

    def wrapped(fn):
        name = fn.__name__
        fn = tag_processor(tag, fn, pass_many, pass_original=pass_original)
        setattr(cls, name, fn)
        cls.__processors__[(tag, pass_many)].append(name)
        return fn

    return wrapped
