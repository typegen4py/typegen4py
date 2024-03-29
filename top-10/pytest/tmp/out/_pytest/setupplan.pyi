from _pytest.config import Config as Config, ExitCode as ExitCode
from _pytest.config.argparsing import Parser as Parser
from _pytest.fixtures import FixtureDef as FixtureDef, SubRequest as SubRequest
from typing import Optional, Union

def pytest_addoption(parser: Parser) -> None: ...
def pytest_fixture_setup(fixturedef: FixtureDef[object], request: SubRequest) -> Optional[object]: ...
def pytest_cmdline_main(config: Config) -> Optional[Union[int, ExitCode]]: ...
