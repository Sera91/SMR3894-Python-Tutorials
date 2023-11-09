import timeit as timeit

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

iterations= 100
total_time = timeit("fib(30)", number=iterations, globals=globals())
f"Average time is {total_time / iterations:.2f} seconds"
