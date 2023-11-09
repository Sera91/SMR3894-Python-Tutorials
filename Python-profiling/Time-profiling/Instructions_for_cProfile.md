# Intro to cProfile

cProfile is one of the two standard profiler for Python. This means that you do not need to install it but it's already provided with the standad Python distribution.
It is a deterministic profiler.



# Profiling code
We are profiling a code which generates random numbers "random_numbers.py":

$ python -m cProfile -o random.prof random_numbers.py

If we run only

$ python -m cProfile random_numbers.py

it prints directly the output to the screen



# Plotting profile

To visualize the output of the profiler in a nice graphical format we can use Snakeviz

$ snakeviz random.prof

