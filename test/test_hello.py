from lessons.hello import hello


def test_default():
    assert hello() == "hello, world"
