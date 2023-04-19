from _pytest.reports import CollectReport as CollectReport, TestReport as TestReport
from typing import Dict, Sequence, Tuple, Union

def assertoutcome(outcomes: Tuple[Sequence[TestReport], Sequence[Union[CollectReport, TestReport]], Sequence[Union[CollectReport, TestReport]]], passed: int=..., skipped: int=..., failed: int=...) -> None: ...
def assert_outcomes(outcomes: Dict[str, int], passed: int=..., skipped: int=..., failed: int=..., errors: int=..., xpassed: int=..., xfailed: int=...) -> None: ...