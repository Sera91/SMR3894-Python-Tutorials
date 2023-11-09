# Intro to line_profiler
The line\_profiler provides three alternative to profile a Python code:

- Kernprof from shell
- using LineProfiler object in code
- %lprun in Jupyter notebooks

The "kernprof" command lets us profile code/script/program using either "cProfile" or "line-by-line profiler". To profiler code using line by line profiler, we need to provide option '-l' or '-line-by-line' else it'll use "cProfile".

# Running Kernprof on a python script
Kernprof -l random_numbers.py
python -m line_profiler random_number_average.py.lprof

## with dat file as output

kernprof -l -o random_generator.dat random_number_average.py

To show the profiled stats we can run:

$ python -m line_profiler random_generator.dat

Let's take a look at the output file:

$ cat random_generator.dat

# Explanation of Resulted Table Columns

The outputted table contains 5 columns:


-    Hits: The first column represents how many times that line was hit inside that function. In our current example hits has a value of 1 but it can be more than one in case of recurrence.
-    Time: The second column represents the time taken by that line in total for all hits. This time is as per set unit. The default unit is 1e-6 which will record time in microseconds. To get data in seconds, we'll have to divide it by 1e6. We have later explained how to change this measurement unit.
-    Per Hit: The third column represents time taken per each call of that line.
-   % Time: The fourth column represents % of time taken by that line of total function time.
-    Line Contents: The fifth column represents a line of function.






