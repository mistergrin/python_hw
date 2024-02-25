import functools
import tracemalloc


def usage_memory(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        memory_current, memory_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Memory used: {memory_peak} B")
        return result
    return wrapper


@usage_memory
def count_factorial(number):
    if number in (0, 1):
        return 1
    result = 1
    for numbers in range(1, number+1):
        result *= numbers
    return result

