import argparse
import py
from _pytest.compat import final as final
from _pytest.config.exceptions import UsageError as UsageError
from typing import Any, Callable, Dict, List, Mapping, NoReturn, Optional, Sequence, Tuple, Union
from typing_extensions import Literal as Literal

FILE_OR_DIR: str

class Parser:
    prog: Optional[str] = ...
    extra_info: Any = ...
    def __init__(self, usage: Optional[str]=..., processopt: Optional[Callable[[Argument], None]]=...) -> None: ...
    def processoption(self, option: Argument) -> None: ...
    def getgroup(self, name: str, description: str=..., after: Optional[str]=...) -> OptionGroup: ...
    def addoption(self, *opts: str, **attrs: Any) -> None: ...
    optparser: Any = ...
    def parse(self, args: Sequence[Union[str, py.path.local]], namespace: Optional[argparse.Namespace]=...) -> argparse.Namespace: ...
    def parse_setoption(self, args: Sequence[Union[str, py.path.local]], option: argparse.Namespace, namespace: Optional[argparse.Namespace]=...) -> List[str]: ...
    def parse_known_args(self, args: Sequence[Union[str, py.path.local]], namespace: Optional[argparse.Namespace]=...) -> argparse.Namespace: ...
    def parse_known_and_unknown_args(self, args: Sequence[Union[str, py.path.local]], namespace: Optional[argparse.Namespace]=...) -> Tuple[argparse.Namespace, List[str]]: ...
    def addini(self, name: str, help: str, type: Optional[Literal[string, pathlist, args, linelist, bool]]=..., default: Any=...) -> None: ...

class ArgumentError(Exception):
    msg: Any = ...
    option_id: Any = ...
    def __init__(self, msg: str, option: Union[Argument, str]) -> None: ...

class Argument:
    type: Any = ...
    default: Any = ...
    dest: Any = ...
    def __init__(self, *names: str, **attrs: Any) -> None: ...
    def names(self) -> List[str]: ...
    def attrs(self) -> Mapping[str, Any]: ...

class OptionGroup:
    name: Any = ...
    description: Any = ...
    options: Any = ...
    parser: Any = ...
    def __init__(self, name: str, description: str=..., parser: Optional[Parser]=...) -> None: ...
    def addoption(self, *optnames: str, **attrs: Any) -> None: ...

class MyOptionParser(argparse.ArgumentParser):
    extra_info: Any = ...
    def __init__(self, parser: Parser, extra_info: Optional[Dict[str, Any]]=..., prog: Optional[str]=...) -> None: ...
    def error(self, message: str) -> NoReturn: ...
    def parse_args(self, args: Optional[Sequence[str]]=..., namespace: Optional[argparse.Namespace]=...) -> argparse.Namespace: ...

class DropShorterLongHelpFormatter(argparse.HelpFormatter):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
