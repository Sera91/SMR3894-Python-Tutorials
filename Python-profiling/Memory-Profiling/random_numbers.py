## random_number_generator.py

import time
import numpy as np

@profile
def very_slow_random_generator():
    time.sleep(5)
    arr1 = np.random.randint(1,100, size=(1000,1000))
    avg = arr1.mean()
    return avg

@profile
def slow_random_generator():
    time.sleep(2)
    arr1 = np.random.randint(1,100, size=(1000,1000))
    avg = arr1.mean()
    return avg

@profile
def fast_random_generator():
    time.sleep(1)
    arr1 = np.random.randint(1,100, size=(1000,1000))
    avg = arr1.mean()
    return avg

@profile
def main_func():
    avg1 = fast_random_generator()
    avg2 = slow_random_generator()
    avg3 = very_slow_random_generator()

    print("Averages: {:.3f}, {:.3f}, {:.3f}".format(avg1,avg2,avg3))

if __name__ == '__main__':
    main_func()
