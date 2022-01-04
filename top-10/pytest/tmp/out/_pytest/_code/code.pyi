import py
from _pytest._code.source import Source as Source, findsource as findsource, getrawcode as getrawcode, getstatementrange_ast as getstatementrange_ast
from _pytest._io import TerminalWriter as TerminalWriter
from _pytest._io.saferepr import safeformat as safeformat, saferepr as saferepr
from _pytest.compat import final as final, get_real_func as get_real_func
from types import CodeType, FrameType, TracebackType
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Pattern, Sequence, Tuple, Type, Union
from typing_extensions import Literal
from weakref import ReferenceType

class Code:
    raw: Any = ...
    def __init__(self, obj: CodeType) -> None: ...
    @classmethod
    def from_function(cls: Any, obj: object) -> Code: ...
    def __eq__(self, other: Any) -> Any: ...
    __hash__: Any = ...
    @property
    def firstlineno(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def path(self) -> Union[py.path.local, str]: ...
    @property
    def fullsource(self) -> Optional[Source]: ...
    def source(self) -> Source: ...
    def getargs(self, var: bool=...) -> Tuple[str, ...]: ...

class Frame:
    raw: Any = ...
    def __init__(self, frame: FrameType) -> None: ...
    @property
    def lineno(self) -> int: ...
    @property
    def f_globals(self) -> Dict[str, Any]: ...
    @property
    def f_locals(self) -> Dict[str, Any]: ...
    @property
    def code(self) -> Code: ...
    @property
    def statement(self) -> Source: ...
    def eval(self, code: Any, **vars: Any): ...
    def repr(self, object: object) -> str: ...
    def getargs(self, var: bool=...) -> Any: ...

class TracebackEntry:
    def __init__(self, rawentry: TracebackType, excinfo: Optional[ReferenceType[ExceptionInfo[BaseException]]]=...) -> None: ...
    @property
    def lineno(self) -> int: ...
    def set_repr_style(self, mode: Literal[short, long]) -> None: ...
    @property
    def frame(self) -> Frame: ...
    @property
    def relline(self) -> int: ...
    @property
    def statement(self) -> Source: ...
    @property
    def path(self) -> Union[py.path.local, str]: ...
    @property
    def locals(self) -> Dict[str, Any]: ...
    def getfirstlinesource(self) -> int: ...
    def getsource(self, astcache: Any=...) -> Optional[Source]: ...
    source: Any = ...
    def ishidden(self) -> bool: ...
    @property
    def name(self) -> str: ...

class Traceback(List[TracebackEntry]):
    def __init__(self, tb: Union[TracebackType, Iterable[TracebackEntry]], excinfo: Optional[ReferenceType[ExceptionInfo[BaseException]]]=...) -> None: ...
    def cut(self, path: Any=..., lineno: Optional[int]=..., firstlineno: Optional[int]=..., excludepath: Optional[py.path.local]=...) -> Traceback: ...
    def __getitem__(self, key: int) -> TracebackEntry: ...
    def __getitem__(self, key: slice) -> Traceback: ...
    def __getitem__(self, key: Union[int, slice]) -> Union[TracebackEntry, Traceback]: ...
    def filter(self, fn: Callable[[TracebackEntry], bool]=...) -> Traceback: ...
    def getcrashentry(self) -> TracebackEntry: ...
    def recursionindex(self) -> Optional[int]: ...

co_equal: Any

class ExceptionInfo:
    @classmethod
    def from_exc_info(cls: Any, exc_info: Tuple[Type[_E], _E, TracebackType], exprinfo: Optional[str]=...) -> ExceptionInfo[_E]: ...
    @classmethod
    def from_current(cls: Any, exprinfo: Optional[str]=...) -> ExceptionInfo[BaseException]: ...
    @classmethod
    def for_later(cls: Any) -> ExceptionInfo[_E]: ...
    def fill_unfilled(self, exc_info: Tuple[Type[_E], _E, TracebackType]) -> None: ...
    @property
    def type(self) -> Type[_E]: ...
    @property
    def value(self) -> _E: ...
    @property
    def tb(self) -> TracebackType: ...
    @property
    def typename(self) -> str: ...
    @property
    def traceback(self) -> Traceback: ...
    @traceback.setter
    def traceback(self, value: Traceback) -> None: ...
    def exconly(self, tryshort: bool=...) -> str: ...
    def errisinstance(self, exc: Union[Type[BaseException], Tuple[Type[BaseException], ...]]) -> bool: ...
    def getrepr(self, showlocals: bool=..., style: _TracebackStyle=..., abspath: bool=..., tbfilter: bool=..., funcargs: bool=..., truncate_locals: bool=..., chain: bool=...) -> Union[ReprExceptionInfo, ExceptionChainRepr]: ...
    def match(self, regexp: Union[str, Pattern[str]]) -> Literal[True]: ...
    def __init__(self, excinfo: Any, striptext: Any, traceback: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class FormattedExcinfo:
    flow_marker: str = ...
    fail_marker: str = ...
    showlocals: Any = ...
    style: Any = ...
    abspath: Any = ...
    tbfilter: Any = ...
    funcargs: Any = ...
    truncate_locals: Any = ...
    chain: Any = ...
    astcache: Any = ...
    def repr_args(self, entry: TracebackEntry) -> Optional[ReprFuncArgs]: ...
    def get_source(self, source: Optional[Source], line_index: int=..., excinfo: Optional[ExceptionInfo[BaseException]]=..., short: bool=...) -> List[str]: ...
    def get_exconly(self, excinfo: ExceptionInfo[BaseException], indent: int=..., markall: bool=...) -> List[str]: ...
    def repr_locals(self, locals: Mapping[str, object]) -> Optional[ReprLocals]: ...
    def repr_traceback_entry(self, entry: TracebackEntry, excinfo: Optional[ExceptionInfo[BaseException]]=...) -> ReprEntry: ...
    def repr_traceback(self, excinfo: ExceptionInfo[BaseException]) -> ReprTraceback: ...
    def repr_excinfo(self, excinfo: ExceptionInfo[BaseException]) -> ExceptionChainRepr: ...
    def __init__(self, showlocals: Any, style: Any, abspath: Any, tbfilter: Any, funcargs: Any, truncate_locals: Any, chain: Any, astcache: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class TerminalRepr:
    def toterminal(self, tw: TerminalWriter) -> None: ...
    def __init__(self) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ExceptionRepr(TerminalRepr):
    reprcrash: Optional[ReprFileLocation]
    reprtraceback: ReprTraceback
    sections: Any = ...
    def __attrs_post_init__(self) -> None: ...
    def addsection(self, name: str, content: str, sep: str=...) -> None: ...
    def toterminal(self, tw: TerminalWriter) -> None: ...
    def __init__(self) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ExceptionChainRepr(ExceptionRepr):
    chain: Any = ...
    reprtraceback: Any = ...
    reprcrash: Any = ...
    def __attrs_post_init__(self) -> None: ...
    def toterminal(self, tw: TerminalWriter) -> None: ...
    def __init__(self, chain: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ReprExceptionInfo(ExceptionRepr):
    reprtraceback: Any = ...
    reprcrash: Any = ...
    def toterminal(self, tw: TerminalWriter) -> None: ...
    def __init__(self, reprtraceback: Any, reprcrash: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ReprTraceback(TerminalRepr):
    reprentries: Any = ...
    extraline: Any = ...
    style: Any = ...
    entrysep: str = ...
    def toterminal(self, tw: TerminalWriter) -> None: ...
    def __init__(self, reprentries: Any, extraline: Any, style: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ReprTracebackNative(ReprTraceback):
    style: str = ...
    reprentries: Any = ...
    extraline: Any = ...
    def __init__(self, tblines: Sequence[str]) -> None: ...

class ReprEntryNative(TerminalRepr):
    lines: Any = ...
    style: _TracebackStyle = ...
    def toterminal(self, tw: TerminalWriter) -> None: ...
    def __init__(self, lines: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ReprEntry(TerminalRepr):
    lines: Any = ...
    reprfuncargs: Any = ...
    reprlocals: Any = ...
    reprfileloc: Any = ...
    style: Any = ...
    def toterminal(self, tw: TerminalWriter) -> None: ...
    def __init__(self, lines: Any, reprfuncargs: Any, reprlocals: Any, reprfileloc: Any, style: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ReprFileLocation(TerminalRepr):
    path: Any = ...
    lineno: Any = ...
    message: Any = ...
    def toterminal(self, tw: TerminalWriter) -> None: ...
    def __init__(self, path: Any, lineno: Any, message: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ReprLocals(TerminalRepr):
    lines: Any = ...
    def toterminal(self, tw: TerminalWriter, indent: Any=...) -> None: ...
    def __init__(self, lines: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class ReprFuncArgs(TerminalRepr):
    args: Any = ...
    def toterminal(self, tw: TerminalWriter) -> None: ...
    def __init__(self, args: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def getfslineno(obj: object) -> Tuple[Union[str, py.path.local], int]: ...
def filter_traceback(entry: TracebackEntry) -> bool: ...
