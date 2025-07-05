from calc.calculator import add
import pytest

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_value():
    assert add("5") == 5
    
def test_multiple_numbers_sum():
    assert add("5, 3, 2, 4, 6") == 20
    
def test_handle_NewLine_delimiter_number_sum():
    assert add("5\n, 4, 6") == 15
    
def test_custom_delimiter_semicolonDefault():
     assert add("//;\n1;2") == 3
    