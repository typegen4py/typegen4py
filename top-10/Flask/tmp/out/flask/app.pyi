from . import cli as cli, json as json
from ._compat import integer_types as integer_types, reraise as reraise, string_types as string_types, text_type as text_type
from .config import Config as Config, ConfigAttribute as ConfigAttribute
from .ctx import AppContext as AppContext, RequestContext as RequestContext
from .globals import g as g, request as request, session as session
from .helpers import _PackageBoundObject, find_package as find_package, get_debug_flag as get_debug_flag, get_env as get_env, get_flashed_messages as get_flashed_messages, get_load_dotenv as get_load_dotenv, locked_cached_property as locked_cached_property, url_for as url_for
from .json import jsonify as jsonify
from .logging import create_logger as create_logger
from .sessions import SecureCookieSessionInterface as SecureCookieSessionInterface
from .signals import appcontext_tearing_down as appcontext_tearing_down, got_request_exception as got_request_exception, request_finished as request_finished, request_started as request_started, request_tearing_down as request_tearing_down
from .templating import DispatchingJinjaLoader as DispatchingJinjaLoader, Environment as Environment
from .wrappers import Request as Request, Response as Response
from typing import Any, Optional

def setupmethod(f: Any): ...

class Flask(_PackageBoundObject):
    request_class: Any = ...
    response_class: Any = ...
    jinja_environment: Any = ...
    app_ctx_globals_class: Any = ...
    config_class: Any = ...
    testing: Any = ...
    secret_key: Any = ...
    session_cookie_name: Any = ...
    permanent_session_lifetime: Any = ...
    send_file_max_age_default: Any = ...
    use_x_sendfile: Any = ...
    json_encoder: Any = ...
    json_decoder: Any = ...
    jinja_options: Any = ...
    default_config: Any = ...
    url_rule_class: Any = ...
    url_map_class: Any = ...
    test_client_class: Any = ...
    test_cli_runner_class: Any = ...
    session_interface: Any = ...
    import_name: Any = ...
    template_folder: Any = ...
    root_path: Any = ...
    static_url_path: Any = ...
    static_folder: Any = ...
    instance_path: Any = ...
    config: Any = ...
    view_functions: Any = ...
    error_handler_spec: Any = ...
    url_build_error_handlers: Any = ...
    before_request_funcs: Any = ...
    before_first_request_funcs: Any = ...
    after_request_funcs: Any = ...
    teardown_request_funcs: Any = ...
    teardown_appcontext_funcs: Any = ...
    url_value_preprocessors: Any = ...
    url_default_functions: Any = ...
    template_context_processors: Any = ...
    shell_context_processors: Any = ...
    blueprints: Any = ...
    extensions: Any = ...
    url_map: Any = ...
    subdomain_matching: Any = ...
    def __init__(self, import_name: Any, static_url_path: Optional[Any] = ..., static_folder: str = ..., static_host: Optional[Any] = ..., host_matching: bool = ..., subdomain_matching: bool = ..., template_folder: str = ..., instance_path: Optional[Any] = ..., instance_relative_config: bool = ..., root_path: Optional[Any] = ...) -> None: ...
    def name(self): ...
    @property
    def propagate_exceptions(self): ...
    @property
    def preserve_context_on_exception(self): ...
    def logger(self): ...
    def jinja_env(self): ...
    @property
    def got_first_request(self): ...
    def make_config(self, instance_relative: bool = ...): ...
    def auto_find_instance_path(self): ...
    def open_instance_resource(self, resource: Any, mode: str = ...): ...
    @property
    def templates_auto_reload(self): ...
    @templates_auto_reload.setter
    def templates_auto_reload(self, value: Any) -> None: ...
    def create_jinja_environment(self): ...
    def create_global_jinja_loader(self): ...
    def select_jinja_autoescape(self, filename: Any): ...
    def update_template_context(self, context: Any) -> None: ...
    def make_shell_context(self): ...
    env: Any = ...
    @property
    def debug(self): ...
    @debug.setter
    def debug(self, value: Any) -> None: ...
    def run(self, host: Optional[Any] = ..., port: Optional[Any] = ..., debug: Optional[Any] = ..., load_dotenv: bool = ..., **options: Any) -> None: ...
    def test_client(self, use_cookies: bool = ..., **kwargs: Any): ...
    def test_cli_runner(self, **kwargs: Any): ...
    def open_session(self, request: Any): ...
    def save_session(self, session: Any, response: Any): ...
    def make_null_session(self): ...
    def register_blueprint(self, blueprint: Any, **options: Any) -> None: ...
    def iter_blueprints(self): ...
    def add_url_rule(self, rule: Any, endpoint: Optional[Any] = ..., view_func: Optional[Any] = ..., provide_automatic_options: Optional[Any] = ..., **options: Any) -> None: ...
    def route(self, rule: Any, **options: Any): ...
    def endpoint(self, endpoint: Any): ...
    def errorhandler(self, code_or_exception: Any): ...
    def register_error_handler(self, code_or_exception: Any, f: Any) -> None: ...
    def template_filter(self, name: Optional[Any] = ...): ...
    def add_template_filter(self, f: Any, name: Optional[Any] = ...) -> None: ...
    def template_test(self, name: Optional[Any] = ...): ...
    def add_template_test(self, f: Any, name: Optional[Any] = ...) -> None: ...
    def template_global(self, name: Optional[Any] = ...): ...
    def add_template_global(self, f: Any, name: Optional[Any] = ...) -> None: ...
    def before_request(self, f: Any): ...
    def before_first_request(self, f: Any): ...
    def after_request(self, f: Any): ...
    def teardown_request(self, f: Any): ...
    def teardown_appcontext(self, f: Any): ...
    def context_processor(self, f: Any): ...
    def shell_context_processor(self, f: Any): ...
    def url_value_preprocessor(self, f: Any): ...
    def url_defaults(self, f: Any): ...
    def handle_http_exception(self, e: Any): ...
    def trap_http_exception(self, e: Any): ...
    def handle_user_exception(self, e: Any): ...
    def handle_exception(self, e: Any): ...
    def log_exception(self, exc_info: Any) -> None: ...
    def raise_routing_exception(self, request: Any) -> None: ...
    def dispatch_request(self): ...
    def full_dispatch_request(self): ...
    def finalize_request(self, rv: Any, from_error_handler: bool = ...): ...
    def try_trigger_before_first_request_functions(self) -> None: ...
    def make_default_options_response(self): ...
    def should_ignore_error(self, error: Any): ...
    def make_response(self, rv: Any): ...
    def create_url_adapter(self, request: Any): ...
    def inject_url_defaults(self, endpoint: Any, values: Any) -> None: ...
    def handle_url_build_error(self, error: Any, endpoint: Any, values: Any): ...
    def preprocess_request(self): ...
    def process_response(self, response: Any): ...
    def do_teardown_request(self, exc: Any = ...) -> None: ...
    def do_teardown_appcontext(self, exc: Any = ...) -> None: ...
    def app_context(self): ...
    def request_context(self, environ: Any): ...
    def test_request_context(self, *args: Any, **kwargs: Any): ...
    def wsgi_app(self, environ: Any, start_response: Any): ...
    def __call__(self, environ: Any, start_response: Any): ...
