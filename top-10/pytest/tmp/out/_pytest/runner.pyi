from .reports import BaseReport as BaseReport, CollectErrorRepr as CollectErrorRepr, CollectReport as CollectReport, TestReport as TestReport
from _pytest import timing as timing
from _pytest._code.code import ExceptionChainRepr as ExceptionChainRepr, ExceptionInfo as ExceptionInfo, TerminalRepr as TerminalRepr
from _pytest.compat import final as final
from _pytest.config.argparsing import Parser as Parser
from _pytest.main import Session as Session
from _pytest.nodes import Collector as Collector, Item as Item, Node as Node
from _pytest.outcomes import Exit as Exit, Skipped as Skipped, TEST_OUTCOME as TEST_OUTCOME
from _pytest.terminal import TerminalReporter as TerminalReporter
from typing import Any, Callable, List, Optional, Tuple, Type, TypeVar, Union
from typing_extensions import Literal as Literal

def pytest_addoption(parser: Parser) -> None: ...
def pytest_terminal_summary(terminalreporter: TerminalReporter) -> None: ...
def pytest_sessionstart(session: Session) -> None: ...
def pytest_sessionfinish(session: Session) -> None: ...
def pytest_runtest_protocol(item: Item, nextitem: Optional[Item]) -> bool: ...
def runtestprotocol(item: Item, log: bool=..., nextitem: Optional[Item]=...) -> List[TestReport]: ...
def show_test_item(item: Item) -> None: ...
def pytest_runtest_setup(item: Item) -> None: ...
def pytest_runtest_call(item: Item) -> None: ...
def pytest_runtest_teardown(item: Item, nextitem: Optional[Item]) -> None: ...
def pytest_report_teststatus(report: BaseReport) -> Optional[Tuple[str, str, str]]: ...
def call_and_report(item: Item, when: Literal[setup, call, teardown], log: bool=..., **kwds: Any) -> TestReport: ...
def check_interactive_exception(call: CallInfo[object], report: BaseReport) -> bool: ...
def call_runtest_hook(item: Item, when: Literal[setup, call, teardown], **kwds: Any) -> CallInfo[None]: ...
TResult = TypeVar('TResult', covariant=True)

class CallInfo:
    excinfo: Any = ...
    start: Any = ...
    stop: Any = ...
    duration: Any = ...
    when: Any = ...
    @property
    def result(self) -> TResult: ...
    @classmethod
    def from_call(cls: Any, func: Callable[[], TResult], when: Literal[collect, setup, call, teardown], reraise: Optional[Union[Type[BaseException], Tuple[Type[BaseException], ...]]]=...) -> CallInfo[TResult]: ...
    def __init__(self, result: Any, excinfo: Any, start: Any, stop: Any, duration: Any, when: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def pytest_runtest_makereport(item: Item, call: CallInfo[None]) -> TestReport: ...
def pytest_make_collect_report(collector: Collector) -> CollectReport: ...

class SetupState:
    stack: Any = ...
    def __init__(self) -> None: ...
    def addfinalizer(self, finalizer: Callable[[], object], colitem: Any) -> None: ...
    def teardown_all(self) -> None: ...
    def teardown_exact(self, item: Any, nextitem: Any) -> None: ...
    def prepare(self, colitem: Any) -> None: ...

def collect_one_node(collector: Collector) -> CollectReport: ...