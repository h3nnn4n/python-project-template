from main import always_false, always_true


def test_always_true():
    assert always_true() is True


def test_always_false():
    assert always_false() is False
