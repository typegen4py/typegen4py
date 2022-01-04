from . import filters as filters
from .asyncsupport import auto_aiter as auto_aiter, auto_await as auto_await
from typing import Any, Optional

async def auto_to_seq(value: Any): ...
async def async_select_or_reject(args: Any, kwargs: Any, modfunc: Any, lookup_attr: Any) -> None: ...
def dualfilter(normal_filter: Any, async_filter: Any): ...
def asyncfiltervariant(original: Any): ...
async def do_first(environment: Any, seq: Any): ...
async def do_groupby(environment: Any, value: Any, attribute: Any): ...
async def do_join(eval_ctx: Any, value: Any, d: str = ..., attribute: Optional[Any] = ...): ...
async def do_list(value: Any): ...
async def do_reject(*args: Any, **kwargs: Any): ...
async def do_rejectattr(*args: Any, **kwargs: Any): ...
async def do_select(*args: Any, **kwargs: Any): ...
async def do_selectattr(*args: Any, **kwargs: Any): ...
async def do_map(*args: Any, **kwargs: Any) -> None: ...
async def do_sum(environment: Any, iterable: Any, attribute: Optional[Any] = ..., start: int = ...): ...
async def do_slice(value: Any, slices: Any, fill_with: Optional[Any] = ...): ...

ASYNC_FILTERS: Any
