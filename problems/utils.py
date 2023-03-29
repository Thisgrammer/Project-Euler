from time import time

def how_long(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'The function {func.__name__} takes {end - start:.6f} seconds to execute')
        return result
    return wrapper