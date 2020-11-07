from __future__ import annotations
import logging
import typing as t
import typing_extensions as tx
from prestring.python import Module, Symbol, FromStatement

InputData = t.Dict[str, t.Any]

logger = logging.getLogger(__name__)


class Context:
    def __init__(
        self,
        *,
        m: t.Optional[Module] = None,
        im: t.Optional[Module] = None,
        relative_imported: t.Optional[t.Dict[str, Symbol]] = None,
        separated: bool = False,
    ):
        self.m: Module = m or Module()
        self.im: Module = im or self.m.submodule()
        self.separated = separated
        self._relative_imported = relative_imported
        if relative_imported is None:
            self._relative_imported = {}

    def from_(self, module: str, name: str) -> FromStatement:
        logger.debug("      import: module=%s, name=%s", module, name)
        return self.im.from_(module, name)

    def import_(self, module: str) -> Symbol:
        logger.debug("      import: module=%s", module)
        return self.im.import_(module)

    def relative_import(self, name: str) -> None:
        if not self.separated:
            return

        imported = self._relative_imported.get(name)
        if imported is not None:
            return None
        logger.debug("      relative import: module=.%s	symbol:%s", name, name)
        self._relative_imported[name] = self.im.from_("." + name, name)
        return None

    def new_child(self) -> Context:
        return self.__class__(
            m=self.m.submodule(newline=False),
            im=self.im,
            relative_imported=self._relative_imported,
            separated=self.separated,
        )


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
            ctx = self._files[name] = Context(separated=True)
            ctx._relative_imported[name] = Symbol(name)
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
