from _pytest.deprecated import PYTEST_COLLECT_MODULE as PYTEST_COLLECT_MODULE
from types import ModuleType
from typing import Any, List

COLLECT_FAKEMODULE_ATTRIBUTES: Any

class FakeCollectModule(ModuleType):
    def __init__(self) -> None: ...
    def __dir__(self) -> List[str]: ...
    def __getattr__(self, name: str) -> Any: ...
