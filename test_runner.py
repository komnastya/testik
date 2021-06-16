def run_tests(module_list):
    for test_function in find_test_functions(module_list):
        try:
            test_function()
            test_result(test_function)
        except AssertionError as ex:
            test_result(test_function, ex)


def find_test_functions(module_list):
    test_functions = []
    for module in module_list:
        for function_name in dir(module):
            if function_name.startswith("test_"):
                value = getattr(module, function_name)
                if callable(value):
                    test_functions.append(value)
    return test_functions


def test_result(test_function, ex=None):
    function_name = test_function.__name__
    if ex is None:
        print(f'\nTest function "{function_name}" run successfully!')
    else:
        print(f'\nTest function "{function_name}" failed!', ex)
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
