# Intro to memory_profiler


The memory profiler is written totally in Python and monitors memory usage by processes as well as line-by-line memory usage by Python programs. It works almost like line_profiler which profiles time. The library is built on top of psutil module of python.

Ways to Profile Memory Usage Of Python Code using "memory_profiler"

    "@profile Decorator" (Covered in Sections 1-3 Below):
        Let us profile memory usage of individual Python functions. Provide statistics showing memory usage by an individual line of python code.
    "mprof Shell/Command Line Command" (Covered in Sections 4-7):
        Let us profile memory usage of whole Python script (".py" file) as a function of time. It'll let us analyze memory usage during code run time rather than by individual line of code.
    "memory_usage() function" (Covered in Section 8):
        Let us profile memory usage of process, python statements, and Python functions for a specified time interval.
    "mprun & memit cell/line Magic commands of Jupyter notebook


#Plotting output
After running:
mprof run random_numbers.py
we can plot the stats using
mprof plot

# Profiling using function decorators

python example_decorator.py



