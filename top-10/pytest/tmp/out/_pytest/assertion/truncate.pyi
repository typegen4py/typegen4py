from _pytest.nodes import Item as Item
from typing import Any, List, Optional

DEFAULT_MAX_LINES: int
DEFAULT_MAX_CHARS: Any
USAGE_MSG: str

def truncate_if_required(explanation: List[str], item: Item, max_length: Optional[int]=...) -> List[str]: ...
