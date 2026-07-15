import time
import functools
from typing import Callable

def timer(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"функция {func.__name__} выполнилась за {end-start} сек.")
        return res
    return wrapper

@timer
def sum_numbers():
    sum_of_one_million = 0
    for n in range(1, 1_000_001):
        sum_of_one_million += n
    return sum_of_one_million

print(sum_numbers())