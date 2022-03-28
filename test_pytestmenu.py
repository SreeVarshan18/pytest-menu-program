import pytestmenu

import pytest


def test_squarearea():
    a = 10
    res = pytestmenu.squarearea(a)
    assert res == a*a


@pytest.mark.filterwarnings
def test_rectperimeter():
    a = 10
    b = 20
    res = pytestmenu.rectperimeter(a, b)
    assert res == 2 * (a + b)


@pytest.mark.filterwarnings
def test_rectarea():
    a = 10
    b =5
    res = pytestmenu.rectarea(a, b)
    assert res == a * b
