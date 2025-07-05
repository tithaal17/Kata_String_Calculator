from calc.calculator import add
import pytest
def test_empty_string_returns_zero():
    assert add("") == 0