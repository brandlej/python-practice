from plates import is_valid


def test_is_valid_min_characters():
    assert is_valid("a") == False


def test_is_valid_max_characters():
    assert is_valid("abcdefg") == False


def test_is_valid_number_start():
    assert is_valid("w0asdf") == False


def test_is_valid_number_middle():
    assert is_valid("asd2fe") == False


def test_is_valid_period():
    assert is_valid("asd.fe") == False


def test_is_valid_space():
    assert is_valid("asd fe") == False


def test_is_valid_correct():
    assert is_valid("abd123") == True
