from typing import Any

class CORSRequestMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class CORSResponseMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
