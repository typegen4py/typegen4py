from ._compat import PY2 as PY2, abc as abc, imap as imap, implements_iterator as implements_iterator, implements_to_string as implements_to_string, iteritems as iteritems, string_types as string_types, text_type as text_type, with_metaclass as with_metaclass
from .exceptions import TemplateNotFound as TemplateNotFound, TemplateRuntimeError as TemplateRuntimeError, UndefinedError as UndefinedError
from .nodes import EvalContext as EvalContext
from .utils import Namespace as Namespace, concat as concat, evalcontextfunction as evalcontextfunction, internalcode as internalcode, missing as missing, object_type_repr as object_type_repr
from markupsafe import escape as escape
from typing import Any, Optional

exported: Any
to_string = text_type

def identity(x: Any): ...
def markup_join(seq: Any): ...
def unicode_join(seq: Any): ...
def new_context(environment: Any, template_name: Any, blocks: Any, vars: Optional[Any] = ..., shared: Optional[Any] = ..., globals: Optional[Any] = ..., locals: Optional[Any] = ...): ...

class TemplateReference:
    def __init__(self, context: Any) -> None: ...
    def __getitem__(self, name: Any): ...

class ContextMeta(type):
    def __new__(mcs: Any, name: Any, bases: Any, d: Any): ...

def resolve_or_missing(context: Any, key: Any, missing: Any = ...): ...

class Context:
    parent: Any = ...
    vars: Any = ...
    environment: Any = ...
    eval_ctx: Any = ...
    exported_vars: Any = ...
    name: Any = ...
    blocks: Any = ...
    def __init__(self, environment: Any, parent: Any, name: Any, blocks: Any) -> None: ...
    def super(self, name: Any, current: Any): ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def resolve(self, key: Any): ...
    def resolve_or_missing(self, key: Any): ...
    def get_exported(self): ...
    def get_all(self): ...
    def call(__self: Any, __obj: Any, *args: Any, **kwargs: Any): ...
    def derived(self, locals: Optional[Any] = ...): ...
    keys: Any = ...
    values: Any = ...
    items: Any = ...
    def __contains__(self, name: Any): ...
    def __getitem__(self, key: Any): ...

class BlockReference:
    name: Any = ...
    def __init__(self, name: Any, context: Any, stack: Any, depth: Any) -> None: ...
    @property
    def super(self): ...
    def __call__(self): ...

class LoopContext:
    index0: int = ...
    depth0: Any = ...
    def __init__(self, iterable: Any, undefined: Any, recurse: Optional[Any] = ..., depth0: int = ...) -> None: ...
    @property
    def length(self): ...
    def __len__(self): ...
    @property
    def depth(self): ...
    @property
    def index(self): ...
    @property
    def revindex0(self): ...
    @property
    def revindex(self): ...
    @property
    def first(self): ...
    @property
    def last(self): ...
    @property
    def previtem(self): ...
    @property
    def nextitem(self): ...
    def cycle(self, *args: Any): ...
    def changed(self, *value: Any): ...
    def __iter__(self) -> Any: ...
    def __next__(self): ...
    def __call__(self, iterable: Any): ...

class Macro:
    name: Any = ...
    arguments: Any = ...
    catch_kwargs: Any = ...
    catch_varargs: Any = ...
    caller: Any = ...
    explicit_caller: Any = ...
    def __init__(self, environment: Any, func: Any, name: Any, arguments: Any, catch_kwargs: Any, catch_varargs: Any, caller: Any, default_autoescape: Optional[Any] = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...

class Undefined:
    def __init__(self, hint: Optional[Any] = ..., obj: Any = ..., name: Optional[Any] = ..., exc: Any = ...) -> None: ...
    def __getattr__(self, name: Any): ...
    __add__: Any = ...
    __radd__: Any = ...
    __mul__: Any = ...
    __rmul__: Any = ...
    __div__: Any = ...
    __rdiv__: Any = ...
    __truediv__: Any = ...
    __rtruediv__: Any = ...
    __floordiv__: Any = ...
    __rfloordiv__: Any = ...
    __mod__: Any = ...
    __rmod__: Any = ...
    __pos__: Any = ...
    __neg__: Any = ...
    __call__: Any = ...
    __getitem__: Any = ...
    __lt__: Any = ...
    __le__: Any = ...
    __gt__: Any = ...
    __ge__: Any = ...
    __int__: Any = ...
    __float__: Any = ...
    __complex__: Any = ...
    __pow__: Any = ...
    __rpow__: Any = ...
    __sub__: Any = ...
    __rsub__: Any = ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __nonzero__(self): ...
    __bool__: Any = ...

def make_logging_undefined(logger: Optional[Any] = ..., base: Optional[Any] = ...): ...

class ChainableUndefined(Undefined):
    def __html__(self): ...
    def __getattr__(self, _: Any): ...
    __getitem__: Any = ...

class DebugUndefined(Undefined): ...

class StrictUndefined(Undefined):
    __iter__: Any = ...
    __len__: Any = ...
    __nonzero__: Any = ...
    __eq__: Any = ...
    __ne__: Any = ...
    __bool__: Any = ...
    __hash__: Any = ...
