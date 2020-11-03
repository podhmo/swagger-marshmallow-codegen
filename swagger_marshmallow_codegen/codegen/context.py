import logging
from prestring.python import Module

logger = logging.getLogger(__name__)


class Context:
    def __init__(self, m=None, im=None):
        self.m = m or Module()
        self.im = im or self.m.submodule()

    def from_(self, module, name):
        logger.debug("      import: module=%s, name=%s", module, name)
        self.im.from_(module, name)

    def import_(self, module):
        logger.debug("      import: module=%s", module)
        self.im.import_(module)

    def new_child(self):
        return self.__class__(self.m.submodule(newline=False), self.im)
