from ._compat import abc as abc, fspath as fspath, iteritems as iteritems, string_types as string_types
from .exceptions import TemplateNotFound as TemplateNotFound
from .utils import internalcode as internalcode, open_if_exists as open_if_exists
from types import ModuleType
from typing import Any, Optional

def split_template_path(template: Any): ...

class BaseLoader:
    has_source_access: bool = ...
    def get_source(self, environment: Any, template: Any) -> None: ...
    def list_templates(self) -> None: ...
    def load(self, environment: Any, name: Any, globals: Optional[Any] = ...): ...

class FileSystemLoader(BaseLoader):
    searchpath: Any = ...
    encoding: Any = ...
    followlinks: Any = ...
    def __init__(self, searchpath: Any, encoding: str = ..., followlinks: bool = ...) -> None: ...
    def get_source(self, environment: Any, template: Any): ...
    def list_templates(self): ...

class PackageLoader(BaseLoader):
    encoding: Any = ...
    manager: Any = ...
    filesystem_bound: Any = ...
    provider: Any = ...
    package_path: Any = ...
    def __init__(self, package_name: Any, package_path: str = ..., encoding: str = ...) -> None: ...
    def get_source(self, environment: Any, template: Any): ...
    def list_templates(self): ...

class DictLoader(BaseLoader):
    mapping: Any = ...
    def __init__(self, mapping: Any) -> None: ...
    def get_source(self, environment: Any, template: Any): ...
    def list_templates(self): ...

class FunctionLoader(BaseLoader):
    load_func: Any = ...
    def __init__(self, load_func: Any) -> None: ...
    def get_source(self, environment: Any, template: Any): ...

class PrefixLoader(BaseLoader):
    mapping: Any = ...
    delimiter: Any = ...
    def __init__(self, mapping: Any, delimiter: str = ...) -> None: ...
    def get_loader(self, template: Any): ...
    def get_source(self, environment: Any, template: Any): ...
    def load(self, environment: Any, name: Any, globals: Optional[Any] = ...): ...
    def list_templates(self): ...

class ChoiceLoader(BaseLoader):
    loaders: Any = ...
    def __init__(self, loaders: Any) -> None: ...
    def get_source(self, environment: Any, template: Any): ...
    def load(self, environment: Any, name: Any, globals: Optional[Any] = ...): ...
    def list_templates(self): ...

class _TemplateModule(ModuleType): ...

class ModuleLoader(BaseLoader):
    has_source_access: bool = ...
    module: Any = ...
    package_name: Any = ...
    def __init__(self, path: Any): ...
    @staticmethod
    def get_template_key(name: Any): ...
    @staticmethod
    def get_module_filename(name: Any): ...
    def load(self, environment: Any, name: Any, globals: Optional[Any] = ...): ...