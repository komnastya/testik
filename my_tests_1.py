from assertions import *


def test_something_0():
    a = 5 + 5
    b = 2 * 5
    assert_true(a == b)
    assert_equal(a, b)


def test_something_1():
    a = 5
    b = 10
    assert_true(a != b)
    assert_not_equal(a, b)
    assert_equal(a, b)  # this is the first error!
