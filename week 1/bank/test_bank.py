from bank import value


def test_value_mixed_casing():
    assert value("Hello") == 0


def test_value_lowercase():
    assert value("hello") == 0


def test_value_no_letter_h():
    assert value("dog") == 100


def test_value_starts_with_letter_h():
    assert value("hyah") == 20


def test_value_hello_prefixed():
    assert value("hello there bud") == 0
