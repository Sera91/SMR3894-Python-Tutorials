To profile a Python script from the shell

python -m cProfile [-o output_file] [-s sort_order] (-m module | myscript.py )

To print the statistics generate with the profiler we use pstats


# Profiler calibration 

there is a certain lag when exiting the profiler event handler from the time that the clock’s value was obtained (and then squirreled away), until the user’s code is once again executing. As a result, functions that are called many times, or call many functions, will typically accumulate this error.

We can measure the Profiler bias using the script

Then, we can calibrate it using the measure biased, in three different ways 

-  1) Apply computed bias to all Profile instances created hereafter.
      profile.Profile.bias = your_computed_bias

- 2) Apply computed bias to a specific Profile instance.
     pr = profile.Profile()
     pr.bias = your_computed_bias

- 3) Specify computed bias in instance constructor.
     pr = profile.Profile(bias=your_computed_bias)
