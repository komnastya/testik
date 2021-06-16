# find all test functions

def run_test(module_list):
    functions_to_test = []
    for module in module_list:
        for function in dir(module):
            if function.startswith('test_'):
                functions_to_test.append(getattr(module, function))
    """Finds all functions which begin with `test_` and executes them."""
    for function in functions_to_test:
        if callable(function):
            try:
                function()
                print(f'\nTest function "{function.__name__}" run successfully!')
            except AssertionError as ex:
                print(f'\nTest function "{function.__name__}" failed!', ex)
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
