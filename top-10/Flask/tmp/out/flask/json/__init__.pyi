from itsdangerous import json as _json
from typing import Any, Optional

class JSONEncoder(_json.JSONEncoder):
    def default(self, o: Any): ...

class JSONDecoder(_json.JSONDecoder): ...

def dumps(obj: Any, app: Optional[Any] = ..., **kwargs: Any): ...
def dump(obj: Any, fp: Any, app: Optional[Any] = ..., **kwargs: Any) -> None: ...
def loads(s: Any, app: Optional[Any] = ..., **kwargs: Any): ...
def load(fp: Any, app: Optional[Any] = ..., **kwargs: Any): ...
def htmlsafe_dumps(obj: Any, **kwargs: Any): ...
def htmlsafe_dump(obj: Any, fp: Any, **kwargs: Any) -> None: ...
def jsonify(*args: Any, **kwargs: Any): ...
