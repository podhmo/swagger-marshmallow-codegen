from __future__ import annotations
import logging
import typing as t
import typing_extensions as tx
from prestring.python import Module, Symbol, FromStatement

InputData = t.Dict[str, t.Any]
if t.TYPE_CHECKING:
    from swagger_marshmallow_codegen.resolver import Resolver
logger = logging.getLogger(__name__)


class Context:
    def __init__(
        self,
        *,
        name: str = "",
        m: t.Optional[Module] = None,
        im: t.Optional[Module] = None,
        rim: t.Optional[Module] = None,
        relative_imported: t.Optional[t.Dict[str, Symbol]] = None,
        separated: bool = False,
    ):
        self.name = name
        self.separated = separated

        self.m: Module = m or Module()
        self.im: Module = im or self.m.submodule()
        self.rim: Module = rim or self.m.submodule()

        self._relative_imported = relative_imported
        if relative_imported is None:
            self._relative_imported = {}

    def from_(self, module: str, name: str) -> FromStatement:
        logger.debug("      import: module=%s, name=%s", module, name)
        return self.im.from_(module, name)

    def import_(self, module: str) -> Symbol:
        logger.debug("      import: module=%s", module)
        return self.im.import_(module)

    def relative_import_from_lazy(self, name: str) -> None:
        if not self.separated:
            return

        imported = self._relative_imported.get(name)
        if imported is not None:
            return None
        logger.debug("      relative import lazy: module=.%s	symbol:%s", name, name)
        self._relative_imported[name] = self.rim.from_("._lazy", f"_use{name}")
        return None

    def relative_import(self, name: str) -> None:
        if not self.separated:
            return
        logger.debug("      relative import: module=.%s	symbol:%s", name, name)
        self.rim.from_(f".{name}", name)
        return None

    def use_relative(self, name: str) -> t.Any:
        if not self.separated:
            return f"lambda: {name}()"
        elif self.name == name:
            # self recursion
            return f"lambda: {name}()"
        elif name not in self._relative_imported:
            # inline definition
            return f"lambda: {name}()"
        else:
            return f"_use{name}"

    def new_child(self) -> Context:
        return self.__class__(
            name=self.name,
            m=self.m.submodule(newline=False),
            im=self.im,
            rim=self.rim,
            relative_imported=self._relative_imported,
            separated=self.separated,
        )


@tx.runtime_checkable
class ContextFactory(tx.Protocol):
    setup: t.Optional[t.Callable[[Context], None]]
    teardown: t.Optional[t.Callable[[Resolver], None]]

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

        self.setup = setup
        self.teardown = self._teardown

    def __call__(self, name: str, *, part: t.Optional[str] = None) -> Context:
        ctx = self._files.get(name)
        if ctx is None:
            ctx = self._files[name] = Context(name=name, separated=True)
            ctx._relative_imported[name] = Symbol(name)
            self.setup(ctx)

        sctx = self._parts.get((name, part))
        if sctx is None:
            sctx = self._parts[(name, part)] = ctx.new_child()
        return sctx

    @property
    def files(self) -> t.Iterator[t.Tuple[str, t.Any]]:
        return sorted([(name, ctx.m) for name, ctx in self._files.items()])

    def _teardown(self, resolver: Resolver) -> None:
        names = [name for name, _ in self.files]

        c = self._files["__init__"] = Context(name="__init__", separated=True)
        for name in names:
            c.from_(f".{name}", resolver.resolve_schema_name(name))

        c = self._files["_lazy"] = Context(name="_lazy", separated=True)
        for name in names:
            cls_name = resolver.resolve_schema_name(name)
            with c.m.def_(f"_use{cls_name}"):
                c.m.from_(f".{name}", cls_name)
                c.m.return_(cls_name)


class OneFileContextFactory:
    def __init__(self, ctx: Context, *, setup: t.Callable[[Context], None]) -> None:
        self._parts: t.Dict[t.Optional[str], Context] = {}
        self._root = ctx

        self.setup = setup
        self.setup(ctx)
        self.teardown = None

    def __call__(self, name: str, *, part: t.Optional[str] = None) -> Context:
        ctx = self._parts.get(part)
        if ctx is not None:
            return ctx
        ctx = self._parts[part] = self._root.new_child()
        return ctx

    @property
    def files(self) -> t.Iterator[t.Tuple[str, t.Any]]:
        yield ("", self._root.m)
