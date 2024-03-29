import enum
from _pytest.outcomes import TEST_OUTCOME as TEST_OUTCOME, fail as fail
from typing import Any, Callable, NoReturn, Optional, Tuple, Type, Union
from typing_extensions import Final as Final

class NotSetType(enum.Enum):
    token: int = ...

NOTSET: Final[Any]
REGEX_TYPE: Any

def is_generator(func: object) -> bool: ...
def iscoroutinefunction(func: object) -> bool: ...
def is_async_function(func: object) -> bool: ...
def getlocation(function: Any, curdir: Optional[str]=...) -> str: ...
def num_mock_patch_args(function: Any) -> int: ...
def getfuncargnames(function: Callable[..., Any], *, name: str=..., is_method: bool=..., cls: Optional[type]=...) -> Tuple[str, ...]: ...
def nullcontext() -> None: ...
def get_default_arg_names(function: Callable[..., Any]) -> Tuple[str, ...]: ...

STRING_TYPES: Any

def ascii_escaped(val: Union[bytes, str]) -> str: ...

class _PytestWrapper:
    obj: Any = ...
    def __init__(self, obj: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def get_real_func(obj: Any): ...
def get_real_method(obj: Any, holder: Any): ...
def getimfunc(func: Any): ...
def safe_getattr(object: Any, name: str, default: Any) -> Any: ...
def safe_isclass(obj: object) -> bool: ...

class cached_property:
    func: Any = ...
    __doc__: Any = ...
    def __init__(self, func: Callable[[_S], _T]) -> None: ...
    def __get__(self, instance: None, owner: Optional[Type[_S]]=...) -> cached_property[_S, _T]: ...
    def __get__(self, instance: _S, owner: Optional[Type[_S]]=...) -> _T: ...
    def __get__(self, instance: Any, owner: Optional[Any] = ...): ...

def assert_never(value: NoReturn) -> NoReturn: ...
