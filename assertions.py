def assert_equal(object_A, object_B):
    assert object_A == object_B, "Objects are not equal"


def assert_not_equal(object_A, object_B):
    assert object_A != object_B, "Objects are equal"


def assert_is(object_A, object_B):
    assert object_A is object_B, "Objects are not the same"


def assert_not_is(object_A, object_B):
    assert object_A is not object_B, "Objects are the same"


def assert_true(object):
    assert object, "Object is False"


def assert_false(object):
    assert object, "Object is True"


def assert_none(object):
    assert object is None, "Object is not None"

def assert_not_none(object):
    assert object is not None, 'Object is None'

def assert_not_none(object):
    assert object is not None, "Object is None"


def assert_in(it, elem):
    assert elem in it, "Element is not in the iterator"

def asser_not_in(it, elem):
    assert elem in it, 'Element is iterator'
