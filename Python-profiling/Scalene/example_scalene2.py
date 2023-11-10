import random


def main_func():
    arr1 = [random.randint(1,10) for i in range(100000)]
    arr2 = [random.randint(1,10) for i in range(100000)]
    arr3 = [arr1[i]+arr2[i] for i in range(100000)]
    tot = sum(arr3)
    print(tot)




if __name__ == "__main__":

    from scalene import scalene_profiler

    #Turn profiling on
    scalene_profiler.start()
    
    main_func()

    # Turn profiling off
    scalene_profiler.stop()
