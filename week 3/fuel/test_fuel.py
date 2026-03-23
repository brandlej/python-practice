from fuel import convert, gauge
import pytest


def test_convert_larger_numerator():
    with pytest.raises(ValueError):
        convert("5/4")


def test_convert_invalid_x_int():
    with pytest.raises(ValueError):
        convert("cat/4")


def test_convert_invalid_y_int():
    with pytest.raises(ValueError):
        convert("4/cat")


def test_convert_zero_y_value():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_convert_valid_value():
    assert convert("3/4") == 75


def test_gauge_empty_one():
    assert gauge(1) == "E"


def test_gauge_empty_less_than_one():
    assert gauge(0) == "E"


def test_gauge_empty_ninety_nine():
    assert gauge(99) == "F"


def test_gauge_empty_full():
    assert gauge(100) == "F"


def test_gauge_partial_fill():
    assert gauge(75) == "75%"
