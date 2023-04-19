from datetime import datetime
from os import PathLike as PathLike
from typing import Any, BinaryIO, Callable, Collection, Dict, Iterable, Iterator, List, Mapping, NoReturn, Optional, Set, Tuple, Type, TypeVar, Union
from typing_extensions import Literal as Literal
from wsgiref.types import WSGIEnvironment as WSGIEnvironment

K = TypeVar('K')
V = TypeVar('V')
T = TypeVar('T')

def is_immutable(self) -> NoReturn: ...
def iter_multi_items(mapping: Union[Mapping[K, Union[V, Iterable[V]]], Iterable[Tuple[K, V]]]) -> Iterator[Tuple[K, V]]: ...

class ImmutableListMixin(List[V]):
    def __hash__(self) -> int: ...
    def __delitem__(self, key: Any) -> NoReturn: ...
    def __iadd__(self, other: Any) -> NoReturn: ...
    def __imul__(self, other: Any) -> NoReturn: ...
    def __setitem__(self, key: Any, value: Any) -> NoReturn: ...
    def append(self, value: Any) -> NoReturn: ...
    def remove(self, value: Any) -> NoReturn: ...
    def extend(self, values: Any) -> NoReturn: ...
    def insert(self, pos: Any, value: Any) -> NoReturn: ...
    def pop(self, index: Any=...) -> NoReturn: ...
    def reverse(self) -> NoReturn: ...
    def sort(self, key: Any=..., reverse: Any=...) -> NoReturn: ...

class ImmutableList(ImmutableListMixin[V]): ...

class ImmutableDictMixin(Dict[K, V]):
    @classmethod
    def fromkeys(cls: Any, keys: Iterable[K], value: Optional[V]=...) -> ImmutableDictMixin[K, V]: ...
    def __hash__(self) -> int: ...
    def setdefault(self, key: Any, default: Any=...) -> NoReturn: ...
    def update(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def pop(self, key: Any, default: Any=...) -> NoReturn: ...
    def popitem(self) -> NoReturn: ...
    def __setitem__(self, key: Any, value: Any) -> NoReturn: ...
    def __delitem__(self, key: Any) -> NoReturn: ...
    def clear(self) -> NoReturn: ...

class ImmutableMultiDictMixin(ImmutableDictMixin[K, V]):
    def add(self, key: Any, value: Any) -> NoReturn: ...
    def popitemlist(self) -> NoReturn: ...
    def poplist(self, key: Any) -> NoReturn: ...
    def setlist(self, key: Any, new_list: Any) -> NoReturn: ...
    def setlistdefault(self, key: Any, default_list: Any=...) -> NoReturn: ...

class UpdateDictMixin(Dict[K, V]):
    on_update: Optional[Callable[[UpdateDictMixin[K, V]], None]]
    def setdefault(self, key: K, default: Optional[V]=...) -> V: ...
    def pop(self, key: K) -> V: ...
    def pop(self, key: K, default: Union[V, T]=...) -> Union[V, T]: ...
    def __setitem__(self, key: K, value: V) -> None: ...
    def __delitem__(self, key: K) -> None: ...
    def clear(self) -> None: ...
    def popitem(self) -> Tuple[K, V]: ...
    def update(self, *args: Union[Mapping[K, V], Iterable[Tuple[K, V]]], **kwargs: V) -> None: ...

class TypeConversionDict(Dict[K, V]):
    def get(self, key: K) -> Optional[V]: ...
    def get(self, key: K, default: Union[V, T]=...) -> Union[V, T]: ...
    def get(self, key: K, default: Optional[T]=..., type: Callable[[V], T]=...) -> Optional[T]: ...

class ImmutableTypeConversionDict(ImmutableDictMixin[K, V], TypeConversionDict[K, V]):
    def copy(self) -> TypeConversionDict[K, V]: ...
    def __copy__(self) -> ImmutableTypeConversionDict: ...

class MultiDict(TypeConversionDict[K, V]):
    def __init__(self, mapping: Optional[Union[Mapping[K, Union[V, Iterable[V]]], Iterable[Tuple[K, V]]]]=...) -> None: ...
    def __getitem__(self, item: K) -> V: ...
    def __setitem__(self, key: K, value: V) -> None: ...
    def add(self, key: K, value: V) -> None: ...
    def getlist(self, key: K) -> List[V]: ...
    def getlist(self, key: K, type: Callable[[V], T]=...) -> List[T]: ...
    def setlist(self, key: K, new_list: Iterable[V]) -> None: ...
    def setdefault(self, key: K, default: Optional[V]=...) -> V: ...
    def setlistdefault(self, key: K, default_list: Optional[Iterable[V]]=...) -> List[V]: ...
    def items(self, multi: bool=...) -> Iterator[Tuple[K, V]]: ...
    def lists(self) -> Iterator[Tuple[K, List[V]]]: ...
    def values(self) -> Iterator[V]: ...
    def listvalues(self) -> Iterator[List[V]]: ...
    def copy(self) -> MultiDict[K, V]: ...
    def deepcopy(self, memo: Any=...) -> MultiDict[K, V]: ...
    def to_dict(self) -> Dict[K, V]: ...
    def to_dict(self, flat: Literal[False]) -> Dict[K, List[V]]: ...
    def update(self, mapping: Union[Mapping[K, V], Iterable[Tuple[K, V]]]) -> None: ...
    def pop(self, key: K) -> V: ...
    def pop(self, key: K, default: Union[V, T]=...) -> Union[V, T]: ...
    def popitem(self) -> Tuple[K, V]: ...
    def poplist(self, key: K) -> List[V]: ...
    def popitemlist(self) -> Tuple[K, List[V]]: ...
    def __copy__(self) -> MultiDict[K, V]: ...
    def __deepcopy__(self, memo: Any) -> MultiDict[K, V]: ...

class _omd_bucket:
    prev: Optional[_omd_bucket]
    next: Optional[_omd_bucket]
    key: K
    value: V
    def __init__(self, omd: OrderedMultiDict, key: K, value: V) -> None: ...
    def unlink(self, omd: OrderedMultiDict) -> None: ...

class OrderedMultiDict(MultiDict[K, V]):
    def __init__(self, mapping: Optional[Mapping[K, V]]=...) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, key: K) -> V: ...
    def __setitem__(self, key: K, value: V) -> None: ...
    def __delitem__(self, key: K) -> None: ...
    def keys(self) -> Iterator[K]: ...
    def __iter__(self) -> Iterator[K]: ...
    def values(self) -> Iterator[V]: ...
    def items(self, multi: bool=...) -> Iterator[Tuple[K, V]]: ...
    def lists(self) -> Iterator[Tuple[K, List[V]]]: ...
    def listvalues(self) -> Iterator[List[V]]: ...
    def add(self, key: K, value: V) -> None: ...
    def getlist(self, key: K) -> List[V]: ...
    def getlist(self, key: K, type: Callable[[V], T]=...) -> List[T]: ...
    def setlist(self, key: K, new_list: Iterable[V]) -> None: ...
    def setlistdefault(self, key: K, default_list: Optional[Iterable[V]]=...) -> List[V]: ...
    def update(self, mapping: Union[Mapping[K, V], Iterable[Tuple[K, V]]]) -> None: ...
    def poplist(self, key: K) -> List[V]: ...
    def pop(self, key: K) -> V: ...
    def pop(self, key: K, default: Union[V, T]=...) -> Union[V, T]: ...
    def popitem(self) -> Tuple[K, V]: ...
    def popitemlist(self) -> Tuple[K, List[V]]: ...
HV = Union[str, int]

class Headers(Dict[str, str]):
    def __init__(self, defaults: Optional[Union[Mapping[str, Union[HV, Iterable[HV]]], Iterable[Tuple[str, HV]]]]=...) -> None: ...
    def __getitem__(self, key: str) -> str: ...
    def __getitem__(self, key: int) -> Tuple[str, str]: ...
    def __getitem__(self, key: slice) -> Headers: ...
    def __getitem__(self, key: str, _get_mode: Literal[True]=...) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def get(self, key: str, default: Optional[str]=...) -> Optional[str]: ...
    def get(self, key: str, default: Optional[T]=..., type: Callable[[str], T]=...) -> Optional[T]: ...
    def getlist(self, key: str) -> List[str]: ...
    def getlist(self, key: str, type: Callable[[str], T]) -> List[T]: ...
    def get_all(self, name: str) -> List[str]: ...
    def items(self, lower: bool=...) -> Iterator[Tuple[str, str]]: ...
    def keys(self, lower: bool=...) -> Iterator[str]: ...
    def values(self) -> Iterator[str]: ...
    def extend(self, *args: Union[Mapping[str, Union[HV, Iterable[HV]]], Iterable[Tuple[str, HV]]], **kwargs: Union[HV, Iterable[HV]]) -> None: ...
    def __delitem__(self, key: Union[str, int, slice]) -> None: ...
    def __delitem__(self, key: str, _index_operation: Literal[False]) -> None: ...
    def remove(self, key: str) -> None: ...
    def pop(self, key: str, default: Optional[str]=...) -> str: ...
    def pop(self, key: Optional[int]=..., default: Optional[Tuple[str, str]]=...) -> Tuple[str, str]: ...
    def popitem(self) -> Tuple[str, str]: ...
    def __contains__(self, key: str) -> bool: ...
    def has_key(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...
    def add(self, _key: str, _value: HV, **kw: HV) -> None: ...
    def add_header(self, _key: str, _value: HV, **_kw: HV) -> None: ...
    def clear(self) -> None: ...
    def set(self, _key: str, _value: HV, **kw: HV) -> None: ...
    def setlist(self, key: str, values: Iterable[HV]) -> None: ...
    def setdefault(self, key: str, default: HV) -> str: ...
    def setlistdefault(self, key: str, default: Iterable[HV]) -> None: ...
    def __setitem__(self, key: str, value: HV) -> None: ...
    def __setitem__(self, key: int, value: Tuple[str, HV]) -> None: ...
    def __setitem__(self, key: slice, value: Iterable[Tuple[str, HV]]) -> None: ...
    def update(self, *args: Union[Mapping[str, HV], Iterable[Tuple[str, HV]]], **kwargs: Union[HV, Iterable[HV]]) -> None: ...
    def to_wsgi_list(self) -> List[Tuple[str, str]]: ...
    def copy(self) -> Headers: ...
    def __copy__(self) -> Headers: ...

class ImmutableHeadersMixin(Headers):
    def __delitem__(self, key: Any, _index_operation: bool=...) -> NoReturn: ...
    def __setitem__(self, key: Any, value: Any) -> NoReturn: ...
    def set(self, _key: Any, _value: Any, **kw: Any) -> NoReturn: ...
    def setlist(self, key: Any, values: Any) -> NoReturn: ...
    def add(self, _key: Any, _value: Any, **kw: Any) -> NoReturn: ...
    def add_header(self, _key: Any, _value: Any, **_kw: Any) -> NoReturn: ...
    def remove(self, key: Any) -> NoReturn: ...
    def extend(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def update(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def insert(self, pos: Any, value: Any) -> NoReturn: ...
    def pop(self, key: Any=..., default: Any=...) -> NoReturn: ...
    def popitem(self) -> NoReturn: ...
    def setdefault(self, key: Any, default: Any) -> NoReturn: ...
    def setlistdefault(self, key: Any, default: Any) -> NoReturn: ...

class EnvironHeaders(ImmutableHeadersMixin, Headers):
    environ: WSGIEnvironment
    def __init__(self, environ: WSGIEnvironment) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, key: str, _get_mode: Literal[False]=...) -> str: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...
    def copy(self) -> NoReturn: ...

class CombinedMultiDict(ImmutableMultiDictMixin[K, V], MultiDict[K, V]):
    dicts: List[MultiDict[K, V]]
    def __init__(self, dicts: Optional[Iterable[MultiDict[K, V]]]) -> None: ...
    @classmethod
    def fromkeys(cls: Any, keys: Any, value: Any=...) -> NoReturn: ...
    def __getitem__(self, key: K) -> V: ...
    def get(self, key: K) -> Optional[V]: ...
    def get(self, key: K, default: Union[V, T]=...) -> Union[V, T]: ...
    def get(self, key: K, default: Optional[T]=..., type: Callable[[V], T]=...) -> Optional[T]: ...
    def getlist(self, key: K) -> List[V]: ...
    def getlist(self, key: K, type: Callable[[V], T]=...) -> List[T]: ...
    def keys(self) -> Set[K]: ...
    def __iter__(self) -> Set[K]: ...
    def items(self, multi: bool=...) -> Iterator[Tuple[K, V]]: ...
    def values(self) -> Iterator[V]: ...
    def lists(self) -> Iterator[Tuple[K, List[V]]]: ...
    def listvalues(self) -> Iterator[List[V]]: ...
    def copy(self) -> MultiDict[K, V]: ...
    def to_dict(self) -> Dict[K, V]: ...
    def to_dict(self, flat: Literal[False]) -> Dict[K, List[V]]: ...
    def __contains__(self, key: K) -> bool: ...
    def has_key(self, key: K) -> bool: ...

class FileMultiDict(MultiDict[str, 'FileStorage']):
    def add_file(self, name: str, file: Union[FileStorage, str, BinaryIO], filename: Optional[str]=..., content_type: Optional[str]=...) -> None: ...

class ImmutableDict(ImmutableDictMixin[K, V], Dict[K, V]):
    def copy(self) -> Dict[K, V]: ...
    def __copy__(self) -> ImmutableDict[K, V]: ...

class ImmutableMultiDict(ImmutableMultiDictMixin[K, V], MultiDict[K, V]):
    def copy(self) -> MultiDict[K, V]: ...
    def __copy__(self) -> ImmutableMultiDict[K, V]: ...

class ImmutableOrderedMultiDict(ImmutableMultiDictMixin[K, V], OrderedMultiDict[K, V]):
    def copy(self) -> OrderedMultiDict[K, V]: ...
    def __copy__(self) -> ImmutableOrderedMultiDict[K, V]: ...

class Accept(ImmutableList[Tuple[str, int]]):
    provided: bool
    def __init__(self, values: Optional[Union[Accept, Iterable[Tuple[str, int]]]]=...) -> None: ...
    def __getitem__(self, key: str) -> int: ...
    def __getitem__(self, key: int) -> Tuple[str, int]: ...
    def __getitem__(self, key: slice) -> Iterable[Tuple[str, int]]: ...
    def quality(self, key: str) -> int: ...
    def __contains__(self, value: str) -> bool: ...
    def index(self, key: str) -> int: ...
    def find(self, key: str) -> int: ...
    def values(self) -> Iterator[str]: ...
    def to_header(self) -> str: ...
    def best_match(self, matches: Iterable[str], default: Optional[str]=...) -> Optional[str]: ...
    @property
    def best(self) -> str: ...

class MIMEAccept(Accept):
    @property
    def accept_html(self) -> bool: ...
    @property
    def accept_xhtml(self) -> bool: ...
    @property
    def accept_json(self) -> bool: ...

class LanguageAccept(Accept):
    def best_match(self, matches: Iterable[str], default: Optional[str]=...) -> Optional[str]: ...

class CharsetAccept(Accept): ...

def cache_property(key: str, empty: _OptCPT, type: Type[_CPT]) -> property: ...

class _CacheControl(UpdateDictMixin[str, _OptCPT], Dict[str, _OptCPT]):
    provided: bool
    def __init__(self, values: Union[Mapping[str, _OptCPT], Iterable[Tuple[str, _OptCPT]]]=..., on_update: Optional[Callable[[_CacheControl], None]]=...) -> None: ...
    @property
    def no_cache(self) -> Optional[bool]: ...
    @no_cache.setter
    def no_cache(self, value: Optional[bool]) -> None: ...
    def no_cache(self) -> None: ...
    @property
    def no_store(self) -> Optional[bool]: ...
    @no_store.setter
    def no_store(self, value: Optional[bool]) -> None: ...
    def no_store(self) -> None: ...
    @property
    def max_age(self) -> Optional[int]: ...
    @max_age.setter
    def max_age(self, value: Optional[int]) -> None: ...
    def max_age(self) -> None: ...
    @property
    def no_transform(self) -> Optional[bool]: ...
    @no_transform.setter
    def no_transform(self, value: Optional[bool]) -> None: ...
    def no_transform(self) -> None: ...
    def to_header(self) -> str: ...
    @staticmethod
    def cache_property(key: str, empty: _OptCPT, type: Type[_CPT]) -> property: ...

class RequestCacheControl(ImmutableDictMixin[str, _OptCPT], _CacheControl):
    @property
    def max_stale(self) -> Optional[int]: ...
    @max_stale.setter
    def max_stale(self, value: Optional[int]) -> None: ...
    def max_stale(self) -> None: ...
    @property
    def min_fresh(self) -> Optional[int]: ...
    @min_fresh.setter
    def min_fresh(self, value: Optional[int]) -> None: ...
    def min_fresh(self) -> None: ...
    @property
    def only_if_cached(self) -> Optional[bool]: ...
    @only_if_cached.setter
    def only_if_cached(self, value: Optional[bool]) -> None: ...
    def only_if_cached(self) -> None: ...

class ResponseCacheControl(_CacheControl):
    @property
    def public(self) -> Optional[bool]: ...
    @public.setter
    def public(self, value: Optional[bool]) -> None: ...
    def public(self) -> None: ...
    @property
    def private(self) -> Optional[bool]: ...
    @private.setter
    def private(self, value: Optional[bool]) -> None: ...
    def private(self) -> None: ...
    @property
    def must_revalidate(self) -> Optional[bool]: ...
    @must_revalidate.setter
    def must_revalidate(self, value: Optional[bool]) -> None: ...
    def must_revalidate(self) -> None: ...
    @property
    def proxy_revalidate(self) -> Optional[bool]: ...
    @proxy_revalidate.setter
    def proxy_revalidate(self, value: Optional[bool]) -> None: ...
    def proxy_revalidate(self) -> None: ...
    @property
    def s_maxage(self) -> Optional[int]: ...
    @s_maxage.setter
    def s_maxage(self, value: Optional[int]) -> None: ...
    def s_maxage(self) -> None: ...
    @property
    def immutable(self) -> Optional[bool]: ...
    @immutable.setter
    def immutable(self, value: Optional[bool]) -> None: ...
    def immutable(self) -> None: ...

def csp_property(key: str) -> property: ...

class ContentSecurityPolicy(UpdateDictMixin[str, str], Dict[str, str]):
    @property
    def base_uri(self) -> Optional[str]: ...
    @base_uri.setter
    def base_uri(self, value: Optional[str]) -> None: ...
    def base_uri(self) -> None: ...
    @property
    def child_src(self) -> Optional[str]: ...
    @child_src.setter
    def child_src(self, value: Optional[str]) -> None: ...
    def child_src(self) -> None: ...
    @property
    def connect_src(self) -> Optional[str]: ...
    @connect_src.setter
    def connect_src(self, value: Optional[str]) -> None: ...
    def connect_src(self) -> None: ...
    @property
    def default_src(self) -> Optional[str]: ...
    @default_src.setter
    def default_src(self, value: Optional[str]) -> None: ...
    def default_src(self) -> None: ...
    @property
    def font_src(self) -> Optional[str]: ...
    @font_src.setter
    def font_src(self, value: Optional[str]) -> None: ...
    def font_src(self) -> None: ...
    @property
    def form_action(self) -> Optional[str]: ...
    @form_action.setter
    def form_action(self, value: Optional[str]) -> None: ...
    def form_action(self) -> None: ...
    @property
    def frame_ancestors(self) -> Optional[str]: ...
    @frame_ancestors.setter
    def frame_ancestors(self, value: Optional[str]) -> None: ...
    def frame_ancestors(self) -> None: ...
    @property
    def frame_src(self) -> Optional[str]: ...
    @frame_src.setter
    def frame_src(self, value: Optional[str]) -> None: ...
    def frame_src(self) -> None: ...
    @property
    def img_src(self) -> Optional[str]: ...
    @img_src.setter
    def img_src(self, value: Optional[str]) -> None: ...
    def img_src(self) -> None: ...
    @property
    def manifest_src(self) -> Optional[str]: ...
    @manifest_src.setter
    def manifest_src(self, value: Optional[str]) -> None: ...
    def manifest_src(self) -> None: ...
    @property
    def media_src(self) -> Optional[str]: ...
    @media_src.setter
    def media_src(self, value: Optional[str]) -> None: ...
    def media_src(self) -> None: ...
    @property
    def navigate_to(self) -> Optional[str]: ...
    @navigate_to.setter
    def navigate_to(self, value: Optional[str]) -> None: ...
    def navigate_to(self) -> None: ...
    @property
    def object_src(self) -> Optional[str]: ...
    @object_src.setter
    def object_src(self, value: Optional[str]) -> None: ...
    def object_src(self) -> None: ...
    @property
    def prefetch_src(self) -> Optional[str]: ...
    @prefetch_src.setter
    def prefetch_src(self, value: Optional[str]) -> None: ...
    def prefetch_src(self) -> None: ...
    @property
    def plugin_types(self) -> Optional[str]: ...
    @plugin_types.setter
    def plugin_types(self, value: Optional[str]) -> None: ...
    def plugin_types(self) -> None: ...
    @property
    def report_to(self) -> Optional[str]: ...
    @report_to.setter
    def report_to(self, value: Optional[str]) -> None: ...
    def report_to(self) -> None: ...
    @property
    def report_uri(self) -> Optional[str]: ...
    @report_uri.setter
    def report_uri(self, value: Optional[str]) -> None: ...
    def report_uri(self) -> None: ...
    @property
    def sandbox(self) -> Optional[str]: ...
    @sandbox.setter
    def sandbox(self, value: Optional[str]) -> None: ...
    def sandbox(self) -> None: ...
    @property
    def script_src(self) -> Optional[str]: ...
    @script_src.setter
    def script_src(self, value: Optional[str]) -> None: ...
    def script_src(self) -> None: ...
    @property
    def script_src_attr(self) -> Optional[str]: ...
    @script_src_attr.setter
    def script_src_attr(self, value: Optional[str]) -> None: ...
    def script_src_attr(self) -> None: ...
    @property
    def script_src_elem(self) -> Optional[str]: ...
    @script_src_elem.setter
    def script_src_elem(self, value: Optional[str]) -> None: ...
    def script_src_elem(self) -> None: ...
    @property
    def style_src(self) -> Optional[str]: ...
    @style_src.setter
    def style_src(self, value: Optional[str]) -> None: ...
    def style_src(self) -> None: ...
    @property
    def style_src_attr(self) -> Optional[str]: ...
    @style_src_attr.setter
    def style_src_attr(self, value: Optional[str]) -> None: ...
    def style_src_attr(self) -> None: ...
    @property
    def style_src_elem(self) -> Optional[str]: ...
    @style_src_elem.setter
    def style_src_elem(self, value: Optional[str]) -> None: ...
    def style_src_elem(self) -> None: ...
    @property
    def worker_src(self) -> Optional[str]: ...
    @worker_src.setter
    def worker_src(self, value: Optional[str]) -> None: ...
    def worker_src(self) -> None: ...
    provided: bool
    def __init__(self, values: Union[Mapping[str, str], Iterable[Tuple[str, str]]]=..., on_update: Optional[Callable[[ContentSecurityPolicy], None]]=...) -> None: ...
    def to_header(self) -> str: ...

class CallbackDict(UpdateDictMixin[K, V], Dict[K, V]):
    def __init__(self, initial: Optional[Union[Mapping[K, V], Iterable[Tuple[K, V]]]]=..., on_update: Optional[Callable[[CallbackDict], None]]=...) -> None: ...

class HeaderSet(Set[str]):
    on_update: Optional[Callable[[HeaderSet], None]]
    def __init__(self, headers: Optional[Iterable[str]]=..., on_update: Optional[Callable[[HeaderSet], None]]=...) -> None: ...
    def add(self, header: str) -> None: ...
    def remove(self, header: str) -> None: ...
    def update(self, iterable: Iterable[str]) -> None: ...
    def discard(self, header: str) -> None: ...
    def find(self, header: str) -> int: ...
    def index(self, header: str) -> int: ...
    def clear(self) -> None: ...
    def as_set(self, preserve_casing: bool=...) -> Set[str]: ...
    def to_header(self) -> str: ...
    def __getitem__(self, idx: int) -> str: ...
    def __delitem__(self, idx: int) -> None: ...
    def __setitem__(self, idx: int, value: str) -> None: ...
    def __contains__(self, header: str) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...

class ETags(Collection[str]):
    star_tag: bool
    def __init__(self, strong_etags: Optional[Iterable[str]]=..., weak_etags: Optional[Iterable[str]]=..., star_tag: bool=...) -> None: ...
    def as_set(self, include_weak: bool=...) -> Set[str]: ...
    def is_weak(self, etag: str) -> bool: ...
    def is_strong(self, etag: str) -> bool: ...
    def contains_weak(self, etag: str) -> bool: ...
    def contains(self, etag: str) -> bool: ...
    def contains_raw(self, etag: str) -> bool: ...
    def to_header(self) -> str: ...
    def __call__(self, etag: Optional[str]=..., data: Optional[bytes]=..., include_weak: bool=...) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def __contains__(self, item: str) -> bool: ...

class IfRange:
    etag: Optional[str]
    date: Optional[datetime]
    def __init__(self, etag: Optional[str]=..., date: Optional[datetime]=...) -> None: ...
    def to_header(self) -> str: ...

class Range:
    units: str
    ranges: List[Tuple[int, Optional[int]]]
    def __init__(self, units: str, ranges: List[Tuple[int, Optional[int]]]) -> None: ...
    def range_for_length(self, length: Optional[int]) -> Optional[Tuple[int, int]]: ...
    def make_content_range(self, length: Optional[int]) -> Optional[ContentRange]: ...
    def to_header(self) -> str: ...
    def to_content_range_header(self, length: Optional[int]) -> Optional[str]: ...

class ContentRange:
    on_update: Optional[Callable[[ContentRange], None]]
    def __init__(self, units: Optional[str], start: Optional[int], stop: Optional[int], length: Optional[int]=..., on_update: Optional[Callable[[ContentRange], None]]=...) -> None: ...
    @property
    def units(self) -> Optional[str]: ...
    @units.setter
    def units(self, value: Optional[str]) -> None: ...
    @property
    def start(self) -> Optional[int]: ...
    @start.setter
    def start(self, value: Optional[int]) -> None: ...
    @property
    def stop(self) -> Optional[int]: ...
    @stop.setter
    def stop(self, value: Optional[int]) -> None: ...
    @property
    def length(self) -> Optional[int]: ...
    @length.setter
    def length(self, value: Optional[int]) -> None: ...
    def set(self, start: Optional[int], stop: Optional[int], length: Optional[int]=..., units: Optional[str]=...) -> None: ...
    def unset(self) -> None: ...
    def to_header(self) -> str: ...

class Authorization(ImmutableDictMixin[str, str], Dict[str, str]):
    type: str
    def __init__(self, auth_type: str, data: Optional[Union[Mapping[str, str], Iterable[Tuple[str, str]]]]=...) -> None: ...
    @property
    def username(self) -> Optional[str]: ...
    @property
    def password(self) -> Optional[str]: ...
    @property
    def realm(self) -> Optional[str]: ...
    @property
    def nonce(self) -> Optional[str]: ...
    @property
    def uri(self) -> Optional[str]: ...
    @property
    def nc(self) -> Optional[str]: ...
    @property
    def cnonce(self) -> Optional[str]: ...
    @property
    def response(self) -> Optional[str]: ...
    @property
    def opaque(self) -> Optional[str]: ...
    @property
    def qop(self) -> Optional[str]: ...
    def to_header(self) -> str: ...

def auth_property(name: str, doc: Optional[str]=...) -> property: ...

class WWWAuthenticate(UpdateDictMixin[str, str], Dict[str, str]):
    def __init__(self, auth_type: Optional[str]=..., values: Optional[Union[Mapping[str, str], Iterable[Tuple[str, str]]]]=..., on_update: Optional[Callable[[WWWAuthenticate], None]]=...) -> None: ...
    def set_basic(self, realm: str=...) -> None: ...
    def set_digest(self, realm: str, nonce: str, qop: Iterable[str]=..., opaque: Optional[str]=..., algorithm: Optional[str]=..., stale: bool=...) -> None: ...
    def to_header(self) -> str: ...
    @property
    def type(self) -> Optional[str]: ...
    @type.setter
    def type(self, value: Optional[str]) -> None: ...
    @property
    def realm(self) -> Optional[str]: ...
    @realm.setter
    def realm(self, value: Optional[str]) -> None: ...
    @property
    def domain(self) -> HeaderSet: ...
    @property
    def nonce(self) -> Optional[str]: ...
    @nonce.setter
    def nonce(self, value: Optional[str]) -> None: ...
    @property
    def opaque(self) -> Optional[str]: ...
    @opaque.setter
    def opaque(self, value: Optional[str]) -> None: ...
    @property
    def algorithm(self) -> Optional[str]: ...
    @algorithm.setter
    def algorithm(self, value: Optional[str]) -> None: ...
    @property
    def qop(self) -> HeaderSet: ...
    @property
    def stale(self) -> Optional[bool]: ...
    @stale.setter
    def stale(self, value: Optional[bool]) -> None: ...
    @staticmethod
    def auth_property(name: str, doc: Optional[str]=...) -> property: ...

class FileStorage:
    name: Optional[str]
    stream: BinaryIO
    filename: Optional[str]
    headers: Headers
    def __init__(self, stream: Optional[BinaryIO]=..., filename: Optional[str]=..., name: Optional[str]=..., content_type: Optional[str]=..., content_length: Optional[int]=..., headers: Optional[Headers]=...) -> None: ...
    @property
    def content_type(self) -> str: ...
    @property
    def content_length(self) -> int: ...
    @property
    def mimetype(self) -> str: ...
    @property
    def mimetype_params(self) -> Dict[str, str]: ...
    def save(self, dst: Union[str, PathLike, BinaryIO], buffer_size: int=...) -> None: ...
    def close(self) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...