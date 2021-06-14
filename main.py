# testik

from assertions import *


def test_something_0():
    assert_true(True)


def test_something_1():
    assert_true(True)
    assert_true(True)
    assert_true(False)  # this is the first error!


def test_something_2():
    assert_true(True)
    assert_true(True)
    assert_true(False)  # this is the second error!


# find all test functions
all_items = globals()  # all items in this module


def run_test_functions():
    """Finds all functions which begin with `test_` and executes them."""
    for name, value in all_items.items():
        if callable(value) and name.startswith("test_"):
            try:
                value()
                print(f'\nTest function "{name}" run successfully!')
            except AssertionError as ex:
                print(f'\nTest function "{name}" failed!', ex)
                tb = ex.__traceback__
                index = 0
                while tb is not None:
                    if index > 0:
                        print("---")
                        print("\tfilename", tb.tb_frame.f_code.co_filename)
                        print("\tname", tb.tb_frame.f_code.co_name)
                        print("\tlineno", tb.tb_lineno)
                    tb = tb.tb_next
                    index += 1


run_test_functions()
