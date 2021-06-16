from assertions import *


def test_something_2():
    class Foo():
        pass

    foo = Foo()
    assert_none(foo) #this is the second error!
