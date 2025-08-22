import pytest
from hello.mathy import add, divide

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negatives():
    assert add(-2, -3) == -5

def test_divide_normal_case():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
