def run_tests(module_list):
    for function_name in find_test_functions(module_list):
        try:
            function_name()
            print(f'\nTest function "{function_name.__name__}" run successfully!')
        except AssertionError as ex:
            print(f'\nTest function "{function_name.__name__}" failed!', ex)
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

def find_test_functions(module_list):
    test_functions = []
    for module in module_list:
        for function_name in dir(module):
            if function_name.startswith("test_"):
                value = getattr(module, function_name)
                if callable(value):
                    test_functions.append(value)
    return test_functions
