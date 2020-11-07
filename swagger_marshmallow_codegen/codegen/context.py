from __future__ import annotations
import logging
import typing as t
import typing_extensions as tx
from prestring.python import Module, Symbol, FromStatement

InputData = t.Dict[str, t.Any]

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


@tx.runtime_checkable
class ContextFactory(tx.Protocol):
    setup: t.Optional[t.Callable[[Context], None]]

    def __call__(self, name: str, *, part: t.Optional[str] = None) -> Context:
        ...


@tx.runtime_checkable
class OutputData(tx.Protocol):
    @property
    def files(self) -> t.Iterator[t.Tuple[str, t.Any]]:
        ...


class SeparatedFilesContextFactory:
    def __init__(self, ctx: Context, *, setup: t.Callable[[Context], None]) -> None:
        self._files: t.Dict[str, Context] = {}
        self._parts: t.Dict[t.Tuple[str, t.Optional[str]], Context] = {}
        self._root = ctx
        self._setup = setup

    def __call__(self, name: str, *, part: t.Optional[str] = None) -> Context:
        ctx = self._files.get(name)
        if ctx is None:
            ctx = self._files[name] = Context()
            self._setup(ctx)

        sctx = self._parts.get((name, part))
        if sctx is None:
            sctx = self._parts[(name, part)] = ctx.new_child()
        return sctx

    @property
    def files(self) -> t.Iterator[t.Tuple[str, t.Any]]:
        return sorted([(name, ctx.m) for name, ctx in self._files.items()])


class OneFileContextFactory:
    def __init__(self, ctx: Context, *, setup: t.Callable[[Context], None]) -> None:
        self._parts: t.Dict[t.Optional[str], Context] = {}
        self._root = ctx
        self.setup = setup
        self.setup(ctx)

    def __call__(self, name: str, *, part: t.Optional[str] = None) -> Context:
        ctx = self._parts.get(part)
        if ctx is not None:
            return ctx
        ctx = self._parts[part] = self._root.new_child()
        return ctx

    @property
    def files(self) -> t.Iterator[t.Tuple[str, t.Any]]:
        yield ("", self._root.m)
