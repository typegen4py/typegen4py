import py
from _pytest import fixtures as fixtures, nodes as nodes
from _pytest._code import filter_traceback as filter_traceback, getfslineno as getfslineno
from _pytest._code.code import ExceptionInfo as ExceptionInfo, TerminalRepr as TerminalRepr
from _pytest._io import TerminalWriter as TerminalWriter
from _pytest._io.saferepr import saferepr as saferepr
from _pytest.compat import NOTSET as NOTSET, REGEX_TYPE as REGEX_TYPE, STRING_TYPES as STRING_TYPES, ascii_escaped as ascii_escaped, final as final, get_default_arg_names as get_default_arg_names, get_real_func as get_real_func, getimfunc as getimfunc, getlocation as getlocation, is_async_function as is_async_function, is_generator as is_generator, safe_getattr as safe_getattr, safe_isclass as safe_isclass
from _pytest.config import Config as Config, ExitCode as ExitCode, hookimpl as hookimpl
from _pytest.config.argparsing import Parser as Parser
from _pytest.deprecated import FSCOLLECTOR_GETHOOKPROXY_ISINITPATH as FSCOLLECTOR_GETHOOKPROXY_ISINITPATH
from _pytest.fixtures import FuncFixtureInfo as FuncFixtureInfo, _Scope
from _pytest.main import Session as Session
from _pytest.mark import MARK_GEN as MARK_GEN, ParameterSet as ParameterSet
from _pytest.mark.structures import Mark as Mark, MarkDecorator as MarkDecorator, get_unpacked_marks as get_unpacked_marks, normalize_mark_list as normalize_mark_list
from _pytest.outcomes import fail as fail, skip as skip
from _pytest.pathlib import ImportPathMismatchError as ImportPathMismatchError, import_path as import_path, parts as parts, visit as visit
from _pytest.warning_types import PytestCollectionWarning as PytestCollectionWarning, PytestUnhandledCoroutineWarning as PytestUnhandledCoroutineWarning
from typing import Any, Callable, Iterable, List, Mapping, Optional, Sequence, Tuple, Type, Union
from typing_extensions import Literal as Literal

def pytest_addoption(parser: Parser) -> None: ...
def pytest_cmdline_main(config: Config) -> Optional[Union[int, ExitCode]]: ...
def pytest_generate_tests(metafunc: Metafunc) -> None: ...
def pytest_configure(config: Config) -> None: ...
def async_warn_and_skip(nodeid: str) -> None: ...
def pytest_pyfunc_call(pyfuncitem: Function) -> Optional[object]: ...
def pytest_collect_file(path: py.path.local, parent: nodes.Collector) -> Optional[Module]: ...
def path_matches_patterns(path: py.path.local, patterns: Iterable[str]) -> bool: ...
def pytest_pycollect_makemodule(path: py.path.local, parent: Any) -> Module: ...
def pytest_pycollect_makeitem(collector: PyCollector, name: str, obj: object) -> Any: ...

class PyobjMixin:
    name: str = ...
    parent: Optional[nodes.Node] = ...
    own_markers: List[Mark] = ...
    def getparent(self, cls: Type[nodes._NodeType]) -> Optional[nodes._NodeType]: ...
    def listchain(self) -> List[nodes.Node]: ...
    @property
    def module(self): ...
    @property
    def cls(self): ...
    @property
    def instance(self): ...
    @property
    def obj(self): ...
    @obj.setter
    def obj(self, value: Any) -> None: ...
    def getmodpath(self, stopatmodule: bool=..., includemodule: bool=...) -> str: ...
    def reportinfo(self) -> Tuple[Union[py.path.local, str], int, str]: ...

class _EmptyClass: ...

IGNORED_ATTRIBUTES: Any

class PyCollector(PyobjMixin, nodes.Collector):
    def funcnamefilter(self, name: str) -> bool: ...
    def isnosetest(self, obj: object) -> bool: ...
    def classnamefilter(self, name: str) -> bool: ...
    def istestfunction(self, obj: object, name: str) -> bool: ...
    def istestclass(self, obj: object, name: str) -> bool: ...
    def collect(self) -> Iterable[Union[nodes.Item, nodes.Collector]]: ...

class Module(nodes.File, PyCollector):
    def collect(self) -> Iterable[Union[nodes.Item, nodes.Collector]]: ...

class Package(Module):
    name: Any = ...
    def __init__(self, fspath: py.path.local, parent: nodes.Collector, config: Any=..., session: Any=..., nodeid: Any=...) -> None: ...
    def setup(self) -> None: ...
    def gethookproxy(self, fspath: py.path.local) -> Any: ...
    def isinitpath(self, path: py.path.local) -> bool: ...
    def collect(self) -> Iterable[Union[nodes.Item, nodes.Collector]]: ...

class Class(PyCollector):
    @classmethod
    def from_parent(cls, parent: Any, name: Any, *, obj: Optional[Any] = ...): ...
    def collect(self) -> Iterable[Union[nodes.Item, nodes.Collector]]: ...

class Instance(PyCollector):
    def collect(self) -> Iterable[Union[nodes.Item, nodes.Collector]]: ...
    obj: Any = ...
    def newinstance(self): ...

def hasinit(obj: object) -> bool: ...
def hasnew(obj: object) -> bool: ...

class CallSpec2:
    metafunc: Any = ...
    funcargs: Any = ...
    params: Any = ...
    marks: Any = ...
    indices: Any = ...
    def __init__(self, metafunc: Metafunc) -> None: ...
    def copy(self) -> CallSpec2: ...
    def getparam(self, name: str) -> object: ...
    @property
    def id(self) -> str: ...
    def setmulti2(self, valtypes: Mapping[str, Literal[params, funcargs]], argnames: Sequence[str], valset: Iterable[object], id: str, marks: Iterable[Union[Mark, MarkDecorator]], scopenum: int, param_index: int) -> None: ...

class Metafunc:
    definition: Any = ...
    config: Any = ...
    module: Any = ...
    function: Any = ...
    fixturenames: Any = ...
    cls: Any = ...
    def __init__(self, definition: FunctionDefinition, fixtureinfo: fixtures.FuncFixtureInfo, config: Config, cls: Any=..., module: Any=...) -> None: ...
    def parametrize(self, argnames: Union[str, List[str], Tuple[str, ...]], argvalues: Iterable[Union[ParameterSet, Sequence[object], object]], indirect: Union[bool, Sequence[str]]=..., ids: Optional[Union[Iterable[Union[None, str, float, int, bool]], Callable[[Any], Optional[object]]]]=..., scope: Optional[_Scope]=..., *, _param_mark: Optional[Mark]=...) -> None: ...

def idmaker(argnames: Iterable[str], parametersets: Iterable[ParameterSet], idfn: Optional[Callable[[Any], Optional[object]]]=..., ids: Optional[List[Union[None, str]]]=..., config: Optional[Config]=..., nodeid: Optional[str]=...) -> List[str]: ...
def show_fixtures_per_test(config: Any): ...
def showfixtures(config: Config) -> Union[int, ExitCode]: ...
def write_docstring(tw: TerminalWriter, doc: str, indent: str=...) -> None: ...

class Function(PyobjMixin, nodes.Item):
    obj: Any = ...
    originalname: Any = ...
    callspec: Any = ...
    fixturenames: Any = ...
    def __init__(self, name: str, parent: Any, config: Optional[Config]=..., callspec: Optional[CallSpec2]=..., callobj: Any=..., keywords: Any=..., session: Optional[Session]=..., fixtureinfo: Optional[FuncFixtureInfo]=..., originalname: Optional[str]=...) -> None: ...
    @classmethod
    def from_parent(cls, parent: Any, **kw: Any): ...
    @property
    def function(self): ...
    def runtest(self) -> None: ...
    def setup(self) -> None: ...
    def repr_failure(self, excinfo: ExceptionInfo[BaseException]) -> Union[str, TerminalRepr]: ...

class FunctionDefinition(Function):
    def runtest(self) -> None: ...
    setup: Any = ...
