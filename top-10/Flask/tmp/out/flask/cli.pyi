import click
from ._compat import getargspec as getargspec, itervalues as itervalues, reraise as reraise, text_type as text_type
from .globals import current_app as current_app
from .helpers import get_debug_flag as get_debug_flag, get_env as get_env, get_load_dotenv as get_load_dotenv
from typing import Any, Optional

class NoAppException(click.UsageError): ...

def find_best_app(script_info: Any, module: Any): ...
def call_factory(script_info: Any, app_factory: Any, arguments: Any = ...): ...
def find_app_by_string(script_info: Any, module: Any, app_name: Any): ...
def prepare_import(path: Any): ...
def locate_app(script_info: Any, module_name: Any, app_name: Any, raise_if_not_found: bool = ...): ...
def get_version(ctx: Any, param: Any, value: Any) -> None: ...

version_option: Any

class DispatchingApp:
    loader: Any = ...
    def __init__(self, loader: Any, use_eager_loading: bool = ...) -> None: ...
    def __call__(self, environ: Any, start_response: Any): ...

class ScriptInfo:
    app_import_path: Any = ...
    create_app: Any = ...
    data: Any = ...
    set_debug_flag: Any = ...
    def __init__(self, app_import_path: Optional[Any] = ..., create_app: Optional[Any] = ..., set_debug_flag: bool = ...) -> None: ...
    def load_app(self): ...

pass_script_info: Any

def with_appcontext(f: Any): ...

class AppGroup(click.Group):
    def command(self, *args: Any, **kwargs: Any): ...
    def group(self, *args: Any, **kwargs: Any): ...

class FlaskGroup(AppGroup):
    create_app: Any = ...
    load_dotenv: Any = ...
    set_debug_flag: Any = ...
    def __init__(self, add_default_commands: bool = ..., create_app: Optional[Any] = ..., add_version_option: bool = ..., load_dotenv: bool = ..., set_debug_flag: bool = ..., **extra: Any) -> None: ...
    def get_command(self, ctx: Any, name: Any): ...
    def list_commands(self, ctx: Any): ...
    def main(self, *args: Any, **kwargs: Any): ...

def load_dotenv(path: Optional[Any] = ...): ...
def show_server_banner(env: Any, debug: Any, app_import_path: Any, eager_loading: Any) -> None: ...

class CertParamType(click.ParamType):
    name: str = ...
    path_type: Any = ...
    def __init__(self) -> None: ...
    def convert(self, value: Any, param: Any, ctx: Any): ...

class SeparatedPathType(click.Path):
    def convert(self, value: Any, param: Any, ctx: Any): ...

def run_command(info: Any, host: Any, port: Any, reload: Any, debugger: Any, eager_loading: Any, with_threads: Any, cert: Any, extra_files: Any) -> None: ...
def shell_command() -> None: ...
def routes_command(sort: Any, all_methods: Any): ...

cli: Any

def main(as_module: bool = ...) -> None: ...