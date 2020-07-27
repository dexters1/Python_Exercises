import pytest
from zajednicki_deliliac import dodela_delilaca
from zajednicki_deliliac import zajednicki_delilac

num = None

def setup_module(module):
    global num
    print("----- setup ------")
    num = dodela_delilaca()

def test_setup():
    assert num == zajednicki_delilac(5, 15)

def test_scope():
    print(num)
    assert num == num

def test_invalid_input():
    with pytest.raises(SyntaxError):
        dodela_delilaca()
