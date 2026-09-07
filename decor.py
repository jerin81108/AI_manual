def log_function_call(func):
    """
    A decorator that logs the name of the function before it's called.
    """
    def wrapper(*args, **kwargs):
        print("Calling function:",func.__name__)
        result = func(*args, **kwargs)
        print(f"Finished calling: {func.__name__}")
        return result
    return wrapper

@log_function_call
def greet(name):
    """
    A simple function that greets a person.
    """
    return f"Hello, {name}!"

@log_function_call
def add(a, b):
    """
    A simple function that adds two numbers.
    """
    return a + b

# Using the decorated functions
print(greet("Alice"))
print(add(5, 3))