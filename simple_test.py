import pytest

def add_one(n):
    return n + 1

def test_add_one():
    assert add_one(2) == 3

def test_add_one1():
    assert add_one(3) == 3



"""
# The tests shown below are to illustrate pytest asserts
# it also helps see how verbosity helps (-v and -vv options of pytest)
"""

def str_cmp_test():
    """
     This test will not run!
     (as the method doesn't start with "test_")
    """
    print("Not a test")
    assert "abc" == "adc"


def test_str_cmp():
    """ compare strings """
    assert "abc" == "adc 1 2"


def test_set_cmp():
    """ Compare sets """
    assert set([1, 2, 4, 6]) == set([1, 2, 3, 7, 6])


def test_dict_cmp():
    """ Compare dictionaries """
    assert {'a': 0, 'n': 1} == {'a':0, 'b':1, 'c':0}


def func():
    raise IOError


def test_exception():
    with pytest.raises(IOError):
        func()

