from fuel import convert, gauge
import pytest


# test_function_expected_behavior_when_condition
def test_convert_raises_value_error_when_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/4")


def test_convert_raises_value_error_when_invalid_x():
    with pytest.raises(ValueError):
        convert("cat/4")


def test_convert_raises_value_error_when_invalid_y():
    with pytest.raises(ValueError):
        convert("4/cat")


def test_convert_raises_zero_division_error_when_y_is_zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_convert_returns_75_when_fraction_is_three_fourths():
    assert convert("3/4") == 75


def test_gauge_returns_E_when_percentage_is_one():
    assert gauge(1) == "E"


def test_gauge_returns_E_when_percentage_is_0():
    assert gauge(0) == "E"


def test_gauge_returns_F_when_percentage_is_99():
    assert gauge(99) == "F"


def test_gauge_returns_F_when_percentage_is_100():
    assert gauge(100) == "F"


def test_gauge_returns_percentage_string_when_between_empty_and_full():
    assert gauge(75) == "75%"
