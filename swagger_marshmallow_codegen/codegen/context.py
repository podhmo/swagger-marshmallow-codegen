import logging
from prestring.python import Module, Symbol, FromStatement

logger = logging.getLogger(__name__)


class Context:
    def __init__(self, m=None, im=None):
        self.m: Module = m or Module()
        self.im: Module = im or self.m.submodule()

    def from_(self, module, name) -> FromStatement:
        logger.debug("      import: module=%s, name=%s", module, name)
        return self.im.from_(module, name)

    def import_(self, module) -> Symbol:
        logger.debug("      import: module=%s", module)
        return self.im.import_(module)

    def new_child(self):
        return self.__class__(self.m.submodule(newline=False), self.im)
