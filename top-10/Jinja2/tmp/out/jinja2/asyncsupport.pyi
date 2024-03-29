from .environment import TemplateModule as TemplateModule
from .runtime import LoopContext as LoopContext
from .utils import concat as concat, internalcode as internalcode, missing as missing
from typing import Any, Optional

async def concat_async(async_gen: Any): ...
async def generate_async(self, *args: Any, **kwargs: Any) -> None: ...
def wrap_generate_func(original_generate: Any): ...
async def render_async(self, *args: Any, **kwargs: Any): ...
def wrap_render_func(original_render: Any): ...
def wrap_block_reference_call(original_call: Any): ...
def wrap_macro_invoke(original_invoke: Any): ...
async def get_default_module_async(self): ...
def wrap_default_module(original_default_module: Any): ...
async def make_module_async(self, vars: Optional[Any] = ..., shared: bool = ..., locals: Optional[Any] = ...): ...
def patch_template() -> None: ...
def patch_runtime() -> None: ...
def patch_filters() -> None: ...
def patch_all() -> None: ...
async def auto_await(value: Any): ...
async def auto_aiter(iterable: Any) -> None: ...

class AsyncLoopContext(LoopContext):
    @property
    async def length(self): ...
    @property
    async def revindex0(self): ...
    @property
    async def revindex(self): ...
    @property
    async def last(self): ...
    @property
    async def nextitem(self): ...
    def __aiter__(self): ...
    async def __anext__(self): ...

async def make_async_loop_context(iterable: Any, undefined: Any, recurse: Optional[Any] = ..., depth0: int = ...): ...
