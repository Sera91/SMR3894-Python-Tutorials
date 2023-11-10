import numpy as np

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

iterations= 100

for i in range(iterations):
	fib(30)
