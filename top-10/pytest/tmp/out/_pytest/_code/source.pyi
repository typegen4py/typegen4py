import ast
import types
from typing import Any, Iterable, Iterator, List, Optional, Tuple, Union

class Source:
    lines: Any = ...
    def __init__(self, obj: object=...) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    __hash__: Any = ...
    def __getitem__(self, key: int) -> str: ...
    def __getitem__(self, key: slice) -> Source: ...
    def __getitem__(self, key: Union[int, slice]) -> Union[str, Source]: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def strip(self) -> Source: ...
    def indent(self, indent: str=...) -> Source: ...
    def getstatement(self, lineno: int) -> Source: ...
    def getstatementrange(self, lineno: int) -> Tuple[int, int]: ...
    def deindent(self) -> Source: ...

def findsource(obj: Any) -> Tuple[Optional[Source], int]: ...
def getrawcode(obj: object, trycall: bool=...) -> types.CodeType: ...
def deindent(lines: Iterable[str]) -> List[str]: ...
def get_statement_startend2(lineno: int, node: ast.AST) -> Tuple[int, Optional[int]]: ...
def getstatementrange_ast(lineno: int, source: Source, assertion: bool=..., astnode: Optional[ast.AST]=...) -> Tuple[ast.AST, int, int]: ...
