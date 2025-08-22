import functools


def not_implemented_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        raise NotImplementedError(f"Podklasa musi nadpisać `{func.__name__}`")
    return wrapper
