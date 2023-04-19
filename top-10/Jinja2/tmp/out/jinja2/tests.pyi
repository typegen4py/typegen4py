from ._compat import abc as abc, integer_types as integer_types, string_types as string_types, text_type as text_type
from .runtime import Undefined as Undefined
from typing import Any

number_re: Any
regex_type: Any
test_callable = callable

def test_odd(value: Any): ...
def test_even(value: Any): ...
def test_divisibleby(value: Any, num: Any): ...
def test_defined(value: Any): ...
def test_undefined(value: Any): ...
def test_none(value: Any): ...
def test_boolean(value: Any): ...
def test_false(value: Any): ...
def test_true(value: Any): ...
def test_integer(value: Any): ...
def test_float(value: Any): ...
def test_lower(value: Any): ...
def test_upper(value: Any): ...
def test_string(value: Any): ...
def test_mapping(value: Any): ...
def test_number(value: Any): ...
def test_sequence(value: Any): ...
def test_sameas(value: Any, other: Any): ...
def test_iterable(value: Any): ...
def test_escaped(value: Any): ...
def test_in(value: Any, seq: Any): ...

TESTS: Any