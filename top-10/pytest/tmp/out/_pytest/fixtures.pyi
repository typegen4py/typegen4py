import py
from _pytest import nodes as nodes
from _pytest._code import getfslineno as getfslineno
from _pytest._code.code import FormattedExcinfo as FormattedExcinfo, TerminalRepr as TerminalRepr
from _pytest._io import TerminalWriter as TerminalWriter
from _pytest.compat import NOTSET as NOTSET, assert_never as assert_never, final as final, get_real_func as get_real_func, get_real_method as get_real_method, getfuncargnames as getfuncargnames, getimfunc as getimfunc, getlocation as getlocation, is_generator as is_generator, safe_getattr as safe_getattr
from _pytest.config import Config as Config, _PluggyPlugin
from _pytest.config.argparsing import Parser as Parser
from _pytest.deprecated import FILLFUNCARGS as FILLFUNCARGS, YIELD_FIXTURE as YIELD_FIXTURE, check_ispytest as check_ispytest
from _pytest.main import Session as Session
from _pytest.mark import Mark as Mark, ParameterSet as ParameterSet
from _pytest.mark.structures import MarkDecorator as MarkDecorator
from _pytest.outcomes import TEST_OUTCOME as TEST_OUTCOME, fail as fail
from _pytest.pathlib import absolutepath as absolutepath
from _pytest.python import CallSpec2 as CallSpec2, Function as Function, Metafunc as Metafunc
from _pytest.store import StoreKey as StoreKey
from typing import Any, Callable, Deque, Dict, Iterable, Iterator, List, NoReturn, Optional, Sequence, Tuple, Union

class PseudoFixtureDef:
    cached_result: Any = ...
    scope: Any = ...
    def __init__(self, cached_result: Any, scope: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def pytest_sessionstart(session: Session) -> None: ...
def get_scope_package(node: Any, fixturedef: FixtureDef[object]) -> Any: ...
def get_scope_node(node: nodes.Node, scope: _Scope) -> Optional[Union[nodes.Item, nodes.Collector]]: ...

name2pseudofixturedef_key: Any

def add_funcarg_pseudo_fixture_def(collector: nodes.Collector, metafunc: Metafunc, fixturemanager: FixtureManager) -> None: ...
def getfixturemarker(obj: object) -> Optional[FixtureFunctionMarker]: ...
def get_parametrized_fixture_keys(item: nodes.Item, scopenum: int) -> Iterator[_Key]: ...
def reorder_items(items: Sequence[nodes.Item]) -> List[nodes.Item]: ...
def fix_cache_order(item: nodes.Item, argkeys_cache: Dict[int, Dict[nodes.Item, Dict[_Key, None]]], items_by_argkey: Dict[int, Dict[_Key, Deque[nodes.Item]]]) -> None: ...
def reorder_items_atscope(items: Dict[nodes.Item, None], argkeys_cache: Dict[int, Dict[nodes.Item, Dict[_Key, None]]], items_by_argkey: Dict[int, Dict[_Key, Deque[nodes.Item]]], scopenum: int) -> Dict[nodes.Item, None]: ...
def fillfixtures(function: Function) -> None: ...
def get_direct_param_fixture_func(request: Any): ...

class FuncFixtureInfo:
    argnames: Any = ...
    initialnames: Any = ...
    names_closure: Any = ...
    name2fixturedefs: Any = ...
    def prune_dependency_tree(self) -> None: ...
    def __init__(self, argnames: Any, initialnames: Any, names_closure: Any, name2fixturedefs: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class FixtureRequest:
    fixturename: Any = ...
    scope: str = ...
    def __init__(self, pyfuncitem: Any, *, _ispytest: bool=...) -> None: ...
    @property
    def fixturenames(self) -> List[str]: ...
    @property
    def node(self): ...
    @property
    def config(self) -> Config: ...
    @property
    def function(self): ...
    @property
    def cls(self): ...
    @property
    def instance(self): ...
    @property
    def module(self): ...
    @property
    def fspath(self) -> py.path.local: ...
    @property
    def keywords(self): ...
    @property
    def session(self) -> Session: ...
    def addfinalizer(self, finalizer: Callable[[], object]) -> None: ...
    def applymarker(self, marker: Union[str, MarkDecorator]) -> None: ...
    def raiseerror(self, msg: Optional[str]) -> NoReturn: ...
    def getfixturevalue(self, argname: str) -> Any: ...

class SubRequest(FixtureRequest):
    fixturename: Any = ...
    param: Any = ...
    param_index: Any = ...
    scope: Any = ...
    def __init__(self, request: FixtureRequest, scope: _Scope, param: Any, param_index: int, fixturedef: FixtureDef[object], *, _ispytest: bool=...) -> None: ...
    def addfinalizer(self, finalizer: Callable[[], object]) -> None: ...

scopes: List[_Scope]
scopenum_function: Any

def scopemismatch(currentscope: _Scope, newscope: _Scope) -> bool: ...
def scope2index(scope: str, descr: str, where: Optional[str]=...) -> int: ...

class FixtureLookupError(LookupError):
    argname: Any = ...
    request: Any = ...
    fixturestack: Any = ...
    msg: Any = ...
    def __init__(self, argname: Optional[str], request: FixtureRequest, msg: Optional[str]=...) -> None: ...
    def formatrepr(self) -> FixtureLookupErrorRepr: ...

class FixtureLookupErrorRepr(TerminalRepr):
    tblines: Any = ...
    errorstring: Any = ...
    filename: Any = ...
    firstlineno: Any = ...
    argname: Any = ...
    def __init__(self, filename: Union[str, py.path.local], firstlineno: int, tblines: Sequence[str], errorstring: str, argname: Optional[str]) -> None: ...
    def toterminal(self, tw: TerminalWriter) -> None: ...

def fail_fixturefunc(fixturefunc: Any, msg: str) -> NoReturn: ...
def call_fixture_func(fixturefunc: _FixtureFunc[_FixtureValue], request: FixtureRequest, kwargs: Any) -> _FixtureValue: ...

class FixtureDef:
    baseid: Any = ...
    has_location: Any = ...
    func: Any = ...
    argname: Any = ...
    scopenum: Any = ...
    scope: Any = ...
    params: Any = ...
    argnames: Any = ...
    unittest: Any = ...
    ids: Any = ...
    cached_result: Any = ...
    def __init__(self, fixturemanager: FixtureManager, baseid: Optional[str], argname: str, func: _FixtureFunc[_FixtureValue], scope: Union[_Scope, Callable[[str, Config], _Scope]], params: Optional[Sequence[object]], unittest: bool=..., ids: Optional[Union[Tuple[Union[None, str, float, int, bool], ...], Callable[[Any], Optional[object]]]]=...) -> None: ...
    def addfinalizer(self, finalizer: Callable[[], object]) -> None: ...
    def finish(self, request: SubRequest) -> None: ...
    def execute(self, request: SubRequest) -> _FixtureValue: ...
    def cache_key(self, request: SubRequest) -> object: ...

def resolve_fixture_function(fixturedef: FixtureDef[_FixtureValue], request: FixtureRequest) -> _FixtureFunc[_FixtureValue]: ...
def pytest_fixture_setup(fixturedef: FixtureDef[_FixtureValue], request: SubRequest) -> _FixtureValue: ...
def wrap_function_to_error_out_if_called_directly(function: _FixtureFunction, fixture_marker: FixtureFunctionMarker) -> _FixtureFunction: ...

class FixtureFunctionMarker:
    scope: Any = ...
    params: Any = ...
    autouse: Any = ...
    ids: Any = ...
    name: Any = ...
    def __call__(self, function: _FixtureFunction) -> _FixtureFunction: ...
    def __init__(self, scope: Any, params: Any, autouse: Any, ids: Any, name: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def fixture(fixture_function: _FixtureFunction, *, scope: Union[_Scope, Callable[[str, Config], _Scope]]=..., params: Optional[Iterable[object]]=..., autouse: bool=..., ids: Optional[Union[Iterable[Union[None, str, float, int, bool]], Callable[[Any], Optional[object]]]]=..., name: Optional[str]=...) -> _FixtureFunction: ...
def yield_fixture(fixture_function: Optional[Any] = ..., *args: Any, scope: str = ..., params: Optional[Any] = ..., autouse: bool = ..., ids: Optional[Any] = ..., name: Optional[Any] = ...): ...
def pytestconfig(request: FixtureRequest) -> Config: ...
def pytest_addoption(parser: Parser) -> None: ...

class FixtureManager:
    FixtureLookupError: Any = ...
    FixtureLookupErrorRepr: Any = ...
    session: Any = ...
    config: Any = ...
    def __init__(self, session: Session) -> None: ...
    def getfixtureinfo(self, node: nodes.Node, func: Any, cls: Any, funcargs: bool=...) -> FuncFixtureInfo: ...
    def pytest_plugin_registered(self, plugin: _PluggyPlugin) -> None: ...
    def getfixtureclosure(self, fixturenames: Tuple[str, ...], parentnode: nodes.Node, ignore_args: Sequence[str]=...) -> Tuple[Tuple[str, ...], List[str], Dict[str, Sequence[FixtureDef[Any]]]]: ...
    def pytest_generate_tests(self, metafunc: Metafunc) -> None: ...
    def pytest_collection_modifyitems(self, items: List[nodes.Item]) -> None: ...
    def parsefactories(self, node_or_obj: Any, nodeid: Any=..., unittest: bool=...) -> None: ...
    def getfixturedefs(self, argname: str, nodeid: str) -> Optional[Sequence[FixtureDef[Any]]]: ...
