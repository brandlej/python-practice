from twtter import shorten


def test_shorten_removes_lowercase_vowels():
    assert shorten("twitter") == "twttr"


def test_shorten_removes_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"


def test_shorten_removes_mixedcase_vowels():
    assert shorten("TwItTer") == "TwtTr"


def test_shorten_preserves_punctuation():
    assert shorten("yeah!") == "yh!"


def test_shorten_preserves_no_vowels():
    assert shorten("bzzz") == "bzzz"
