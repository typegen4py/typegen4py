from io import StringIO as StringIO
from os import fspath as fspath
from typing import Any, Optional

PY2: Any
text_type = unicode
string_types: Any
integer_types: Any
text_type = str
iterkeys: Any
itervalues: Any
iteritems: Any

def reraise(tp: Any, value: Any, tb: Optional[Any] = ...) -> None: ...

implements_to_string: Any

def with_metaclass(meta: Any, *bases: Any): ...

BROKEN_PYPY_CTXMGR_EXIT: bool

class _Mgr:
    def __enter__(self): ...
    def __exit__(self, *args: Any) -> None: ...

class _DeprecatedBool:
    message: Any = ...
    value: Any = ...
    def __init__(self, name: Any, version: Any, value: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __bool__(self): ...
    __nonzero__: Any = ...

json_available: Any