def run_tests(module_list):
    for module in module_list:
        before_each, after_each, test_functions = find_test_functions(module)
        for test_function in test_functions:
            if before_each is not None:
                before_each()
            try:
                test_function()
                result = None
            except AssertionError as ex:
                result = ex
            if after_each is not None:
                after_each()
            test_result(test_function, result)


def find_test_functions(module):
    before_each = None
    after_each = None
    test_functions = []
    for function_name in dir(module):
        if function_name == "before_each":
            before_each = getattr(module, function_name)
        if function_name == "after_each":
            after_each = getattr(module, function_name)
        if function_name.startswith("test_"):
            value = getattr(module, function_name)
            if callable(value):
                test_functions.append(value)
    return (before_each, after_each, test_functions)


def test_result(test_function, ex):
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
