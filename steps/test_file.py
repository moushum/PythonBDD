import pytest


def test_01():
    a = 3
    b = 4
    assert a + 1 == b, "test failed"
    assert a == b, "test failed is not eq to b"


def test_02():
    name = "selenium"
    assert name.upper() == "SELENIUM"

@pytest.mark.log
def test_03():
    assert True


def test_04():
    assert False
