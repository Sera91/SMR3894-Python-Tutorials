import time
import random

def very_slow_random_generator():
    time.sleep(5)
    arr = [random.randint(1,100) for i in range(100000)]
    return sum(arr) / len(arr)

def slow_random_generator():
    time.sleep(2)
    arr = [random.randint(1,100) for i in range(100000)]
    return sum(arr) / len(arr)

def fast_random_generator():
    time.sleep(1)
    arr = [random.randint(1,100) for i in range(100000)]
    return sum(arr) / len(arr)


def main_func():
    result = fast_random_generator()
    print(result)

    result = slow_random_generator()
    print(result)

    result = very_slow_random_generator()
    print(result)

main_func()
