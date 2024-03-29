from . import nodes as nodes
from ._compat import iteritems as iteritems, string_types as string_types, with_metaclass as with_metaclass
from .defaults import BLOCK_END_STRING as BLOCK_END_STRING, BLOCK_START_STRING as BLOCK_START_STRING, COMMENT_END_STRING as COMMENT_END_STRING, COMMENT_START_STRING as COMMENT_START_STRING, KEEP_TRAILING_NEWLINE as KEEP_TRAILING_NEWLINE, LINE_COMMENT_PREFIX as LINE_COMMENT_PREFIX, LINE_STATEMENT_PREFIX as LINE_STATEMENT_PREFIX, LSTRIP_BLOCKS as LSTRIP_BLOCKS, NEWLINE_SEQUENCE as NEWLINE_SEQUENCE, TRIM_BLOCKS as TRIM_BLOCKS, VARIABLE_END_STRING as VARIABLE_END_STRING, VARIABLE_START_STRING as VARIABLE_START_STRING
from .environment import Environment as Environment
from .exceptions import TemplateAssertionError as TemplateAssertionError, TemplateSyntaxError as TemplateSyntaxError
from .nodes import ContextReference as ContextReference
from .runtime import concat as concat
from .utils import contextfunction as contextfunction, import_string as import_string
from typing import Any, Optional

GETTEXT_FUNCTIONS: Any

class ExtensionRegistry(type):
    def __new__(mcs: Any, name: Any, bases: Any, d: Any): ...

class Extension:
    tags: Any = ...
    priority: int = ...
    environment: Any = ...
    def __init__(self, environment: Any) -> None: ...
    def bind(self, environment: Any): ...
    def preprocess(self, source: Any, name: Any, filename: Optional[Any] = ...): ...
    def filter_stream(self, stream: Any): ...
    def parse(self, parser: Any) -> None: ...
    def attr(self, name: Any, lineno: Optional[Any] = ...): ...
    def call_method(self, name: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., dyn_args: Optional[Any] = ..., dyn_kwargs: Optional[Any] = ..., lineno: Optional[Any] = ...): ...

class InternationalizationExtension(Extension):
    tags: Any = ...
    def __init__(self, environment: Any) -> None: ...
    def parse(self, parser: Any): ...

class ExprStmtExtension(Extension):
    tags: Any = ...
    def parse(self, parser: Any): ...

class LoopControlExtension(Extension):
    tags: Any = ...
    def parse(self, parser: Any): ...

class WithExtension(Extension): ...
class AutoEscapeExtension(Extension): ...

class DebugExtension(Extension):
    tags: Any = ...
    def parse(self, parser: Any): ...

def extract_from_ast(node: Any, gettext_functions: Any = ..., babel_style: bool = ...) -> None: ...

class _CommentFinder:
    tokens: Any = ...
    comment_tags: Any = ...
    offset: int = ...
    last_lineno: int = ...
    def __init__(self, tokens: Any, comment_tags: Any) -> None: ...
    def find_backwards(self, offset: Any): ...
    def find_comments(self, lineno: Any): ...

def babel_extract(fileobj: Any, keywords: Any, comment_tags: Any, options: Any): ...
i18n = InternationalizationExtension
do = ExprStmtExtension
loopcontrols = LoopControlExtension
with_ = WithExtension
autoescape = AutoEscapeExtension
debug = DebugExtension
