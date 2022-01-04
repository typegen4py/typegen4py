from _pytest.config import Config as Config
from _pytest.config.argparsing import Parser as Parser
from _pytest.nodes import Item as Item
from _pytest.store import StoreKey as StoreKey
from typing import Any, Generator

fault_handler_stderr_key: Any

def pytest_addoption(parser: Parser) -> None: ...
def pytest_configure(config: Config) -> None: ...

class FaultHandlerHooks:
    def pytest_configure(self, config: Config) -> None: ...
    def pytest_unconfigure(self, config: Config) -> None: ...
    @staticmethod
    def get_timeout_config_value(config: Any): ...
    def pytest_runtest_protocol(self, item: Item) -> Generator[None, None, None]: ...
    def pytest_enter_pdb(self) -> None: ...
    def pytest_exception_interact(self) -> None: ...
