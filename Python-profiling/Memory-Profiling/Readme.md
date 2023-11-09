# Intro to memory_profiler


$pip install -U memory_profiler


python -m memory_profiler example.py

Note:If a python script with decorator @profile is called using -m memory_profiler in the command line, the precision parameter is ignored.

# Time-based memory usage reports

The memory_profiler executable can be called from the terminal with the command mprof


The available commands for mprof are:

- mprof run: running an executable, recording memory usage

- mprof plot: plotting one the recorded memory usage (by default, the last one)

- mprof list: listing all recorded memory usage files in a user-friendly way.

- mprof clean: removing all recorded memory usage files.

- mprof rm: removing specific recorded memory usage file

For memory profiling simple code it can be enough to use the %memit magic command in ipython

Sometimes it is useful to have full memory usage reports as a function of time (not line-by-line) of external processes (be it Python scripts or not). In this case the executable mprof might be useful!!

# Running mprof

Launching

$ mprof run –python python example.py

will record timestamps when entering/leaving the profiled function


# Visualizing the report of memory profiler
 running 

$ mprof plot --flame

will plot the result, making plots (using matplotlib) similar to this one:

By default, the command line call is set as the graph title. If you wish to customize it, you can use the -t option to manually set the figure title.

mprof plot -t ‘Recorded memory usage’

You can also hide the function timestamps using the n flag, such as

mprof plot -n

Trend lines and its numeric slope can be plotted using the s flag, such as

mprof plot -s

The intended usage of the -s switch is to check the labels’ numerical slope over a significant time period. For code with:

- s>0 it might mean a memory leak.

- s~0 if 0 or near 0, the memory usage may be considered stable.

- 's<= 0' to be interpreted depending on the expected process memory usage patterns, also might mean that the sampling period is too small.

A discussion on details is available here:
https://fa.bianp.net/blog/2014/plot-memory-usage-as-a-function-of-time/

Help on each mprof subcommand can be obtained with the -h flag, e.g. mprof run -h.

#Forked child processes
In a multiprocessing context the main process will spawn child processes whose system resources are allocated separately from the parent process. This can lead to an inaccurate report of memory usage since by default only the parent process is being tracked. The mprof utility provides two mechanisms to track the usage of child processes: sum the memory of all children to the parent’s usage and track each child individual.

To create a report that combines memory usage of all the children and the parent, use the include-children flag in either the profile decorator or as a command line argument to mprof:

mprof run --include-children

The second method tracks each child independently of the main process, serializing child rows by index to the output stream. Use the multiprocess flag

mprof run --multiprocess <script>
mprof plot

You can combine both the include-children and multiprocess flags to show the total memory of the program as well as each child individually.


# Utilities for app developing
memory_profiler exposes a number of functions to be used in third-party code.

memory_usage(proc=-1, interval=.1, timeout=None) returns the memory usage over a time interval. The first argument, proc represents what should be monitored. This can either be the PID of a process (not necessarily a Python program), a string containing some python code to be evaluated or a tuple (f, args, kw) containing a function and its arguments to be evaluated as f(*args, **kw). For example,



# Warning

If your Python file imports the memory profiler as  "from memory_profiler import profile" these timestamps will not be recorded. Comment out the import, leave your functions decorated, and re-run.

