from .request import Request as Request
from typing import Any

class _FakeSubclassCheck(type):
    def __subclasscheck__(cls, subclass: Any): ...
    def __instancecheck__(cls, instance: Any): ...

class BaseRequest(Request, metaclass=_FakeSubclassCheck):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
