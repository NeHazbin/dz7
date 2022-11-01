def checker(*exc_types):
    def checker(function):
        def checker(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except Exception as exc:
                print(f"We have problems {exc}")
            else:
                print(f"No problems. Result –{result}")
        return checker
    return checker
@checker(NameError, TypeError, SyntaxError)
def calculate(expression):
    return eval(expression)
calculate("2+2")
calculate("2*3")
calculate("2/3")
calculate("2**3")
calculate("2dfgd3")