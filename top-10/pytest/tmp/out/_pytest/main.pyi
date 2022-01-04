import py
from _pytest import nodes as nodes
from _pytest.compat import final as final
from _pytest.config import Config as Config, ExitCode as ExitCode, PytestPluginManager as PytestPluginManager, UsageError as UsageError, directory_arg as directory_arg, hookimpl as hookimpl
from _pytest.config.argparsing import Parser as Parser
from _pytest.fixtures import FixtureManager as FixtureManager
from _pytest.outcomes import exit as exit
from _pytest.pathlib import absolutepath as absolutepath, bestrelpath as bestrelpath, visit as visit
from _pytest.reports import CollectReport as CollectReport, TestReport as TestReport
from _pytest.runner import SetupState as SetupState, collect_one_node as collect_one_node
from pathlib import Path
from typing import Any, Callable, Dict, Iterator, List, Optional, Sequence, Tuple, Union
from typing_extensions import Literal as Literal

def pytest_addoption(parser: Parser) -> None: ...
def validate_basetemp(path: str) -> str: ...
def wrap_session(config: Config, doit: Callable[[Config, Session], Optional[Union[int, ExitCode]]]) -> Union[int, ExitCode]: ...
def pytest_cmdline_main(config: Config) -> Union[int, ExitCode]: ...
def pytest_collection(session: Session) -> None: ...
def pytest_runtestloop(session: Session) -> bool: ...
def pytest_ignore_collect(path: py.path.local, config: Config) -> Optional[bool]: ...
def pytest_collection_modifyitems(items: List[nodes.Item], config: Config) -> None: ...

class FSHookProxy:
    pm: Any = ...
    remove_mods: Any = ...
    def __init__(self, pm: PytestPluginManager, remove_mods: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

class Interrupted(KeyboardInterrupt):
    __module__: str = ...

class Failed(Exception): ...

class _bestrelpath_cache(Dict[Path, str]):
    path: Any = ...
    def __missing__(self, path: Path) -> str: ...
    def __init__(self, path: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class Session(nodes.FSCollector):
    Interrupted: Any = ...
    Failed: Any = ...
    exitstatus: Union[int, ExitCode]
    testsfailed: int = ...
    testscollected: int = ...
    shouldstop: bool = ...
    shouldfail: bool = ...
    trace: Any = ...
    startdir: Any = ...
    def __init__(self, config: Config) -> None: ...
    @classmethod
    def from_config(cls: Any, config: Config) -> Session: ...
    def pytest_collectstart(self) -> None: ...
    def pytest_runtest_logreport(self, report: Union[TestReport, CollectReport]) -> None: ...
    pytest_collectreport: Any = ...
    def isinitpath(self, path: py.path.local) -> bool: ...
    def gethookproxy(self, fspath: py.path.local) -> Any: ...
    def perform_collect(self, args: Optional[Sequence[str]]=..., genitems: Literal[True]=...) -> Sequence[nodes.Item]: ...
    def perform_collect(self, args: Optional[Sequence[str]]=..., genitems: bool=...) -> Sequence[Union[nodes.Item, nodes.Collector]]: ...
    items: Any = ...
    def perform_collect(self, args: Optional[Sequence[str]]=..., genitems: bool=...) -> Sequence[Union[nodes.Item, nodes.Collector]]: ...
    def collect(self) -> Iterator[Union[nodes.Item, nodes.Collector]]: ...
    def genitems(self, node: Union[nodes.Item, nodes.Collector]) -> Iterator[nodes.Item]: ...

def search_pypath(module_name: str) -> str: ...
def resolve_collection_argument(invocation_path: Path, arg: str, *, as_pypath: bool=...) -> Tuple[py.path.local, List[str]]: ...
