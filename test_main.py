from main import always_true, always_false


def test_always_true():
    assert always_true() is True


def test_always_false():
    assert always_false() is False
