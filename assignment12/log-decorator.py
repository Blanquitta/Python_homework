#Task 1
import logging
from functools import wraps

# One-time logger setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

#Task 2
# The logger_decorator definition
def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Format args and kwargs
        pos_args = list(args) if args else "none"
        kw_args = kwargs if kwargs else "none"

        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {pos_args}\n"
            f"keyword parameters: {kw_args}\n"
            f"return: {result}\n"
        )

        logger.log(logging.INFO, log_message)
        return result

    return wrapper

# Sample functions with different parameter types

@logger_decorator
def greet():
    print("Hello, World!")

@logger_decorator
def accept_args(*args):
    return True

@logger_decorator
def keyword_only(**kwargs):
    return logger_decorator

# Mainline code
if __name__ == "__main__":
    greet()
    accept_args(1, 2, 3, "test")
    keyword_only(name="Alice", age=30)


def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

# Mainline code
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  

    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  # Expected behavior