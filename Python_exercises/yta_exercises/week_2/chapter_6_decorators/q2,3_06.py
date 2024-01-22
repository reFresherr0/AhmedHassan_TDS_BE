def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper
