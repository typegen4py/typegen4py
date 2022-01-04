import typing as t
from typing import Any

prefix: Any

class ReloaderLoop:
    name: str = ...
    extra_files: Any = ...
    exclude_patterns: Any = ...
    interval: Any = ...
    def __init__(self, extra_files: t.Optional[t.Iterable[str]]=..., exclude_patterns: t.Optional[t.Iterable[str]]=..., interval: t.Union[int, float]=...) -> None: ...
    def __enter__(self) -> ReloaderLoop: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def run(self) -> None: ...
    def run_step(self) -> None: ...
    def restart_with_reloader(self) -> int: ...
    def trigger_reload(self, filename: str) -> None: ...
    def log_reload(self, filename: str) -> None: ...

class StatReloaderLoop(ReloaderLoop):
    name: str = ...
    mtimes: Any = ...
    def __enter__(self) -> ReloaderLoop: ...
    def run_step(self) -> None: ...

class WatchdogReloaderLoop(ReloaderLoop):
    name: Any = ...
    observer: Any = ...
    event_handler: Any = ...
    should_reload: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def trigger_reload(self, filename: str) -> None: ...
    watches: Any = ...
    def __enter__(self) -> ReloaderLoop: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def run(self) -> None: ...
    def run_step(self) -> None: ...

reloader_loops: t.Dict[str, t.Type[ReloaderLoop]]

def ensure_echo_on() -> None: ...
def run_with_reloader(main_func: t.Callable[[], None], extra_files: t.Optional[t.Iterable[str]]=..., exclude_patterns: t.Optional[t.Iterable[str]]=..., interval: t.Union[int, float]=..., reloader_type: str=...) -> Any: ...
