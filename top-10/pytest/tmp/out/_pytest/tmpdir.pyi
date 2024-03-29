import py
from .pathlib import LOCK_TIMEOUT as LOCK_TIMEOUT, ensure_reset_dir as ensure_reset_dir, make_numbered_dir as make_numbered_dir, make_numbered_dir_with_cleanup as make_numbered_dir_with_cleanup
from _pytest.compat import final as final
from _pytest.config import Config as Config
from _pytest.deprecated import check_ispytest as check_ispytest
from _pytest.fixtures import FixtureRequest as FixtureRequest, fixture as fixture
from _pytest.monkeypatch import MonkeyPatch as MonkeyPatch
from pathlib import Path
from typing import Any, Optional

class TempPathFactory:
    def __init__(self, given_basetemp: Optional[Path], trace: Any, basetemp: Optional[Path]=..., *, _ispytest: bool=...) -> None: ...
    @classmethod
    def from_config(cls: Any, config: Config, *, _ispytest: bool=...) -> TempPathFactory: ...
    def mktemp(self, basename: str, numbered: bool=...) -> Path: ...
    def getbasetemp(self) -> Path: ...
    def __init__(self, given_basetemp: Any, trace: Any, basetemp: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class TempdirFactory:
    def __init__(self, tmppath_factory: TempPathFactory, *, _ispytest: bool=...) -> None: ...
    def mktemp(self, basename: str, numbered: bool=...) -> py.path.local: ...
    def getbasetemp(self) -> py.path.local: ...
    def __init__(self, tmppath_factory: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def get_user() -> Optional[str]: ...
def pytest_configure(config: Config) -> None: ...
def tmpdir_factory(request: FixtureRequest) -> TempdirFactory: ...
def tmp_path_factory(request: FixtureRequest) -> TempPathFactory: ...
def tmpdir(tmp_path: Path) -> py.path.local: ...
def tmp_path(request: FixtureRequest, tmp_path_factory: TempPathFactory) -> Path: ...
