import pytest


def test_firstTest(initialze):
    print("I am First test")

@pytest.mark.run
def test_secondTesABC(initialze):
    print("I am second test")


@pytest.mark.parametrize("a,b,expected",[(1,2,3),(2,2,4),(3,3,6),
                                         (5,5,10)])
def test_checkSum(a,b,expected):
    assert a+b == expected