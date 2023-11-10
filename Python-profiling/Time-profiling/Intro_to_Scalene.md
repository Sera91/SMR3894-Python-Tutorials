![scalene](https://github.com/plasma-umass/scalene/raw/master/docs/scalene-icon-white.png)

# Scalene: a Python CPU+GPU+memory profiler with AI-powered optimization proposals

by [Emery Berger](https://emeryberger.com), [Sam Stern](https://samstern.me/), and [Juan Altmayer Pizzorno](https://github.com/jaltmayerpizzorno).

Scalene is a high-performance CPU, GPU *and* memory profiler for
Python that does a number of things that other Python profilers do not
and cannot do.  It runs orders of magnitude faster than many other
profilers while delivering far more detailed information. It is also
the first profiler ever to incorporate AI-powered proposed
optimizations.


#### Installing Scalene:

```console
python3 -m pip install -U scalene
```

or

```console
conda install -c conda-forge scalene
```

#### Using Scalene:

After installing Scalene, you can use Scalene at the command line, or as a Visual Studio Code extension.


<details>
<summary>
Commonly used command-line options:
</summary>

```console
scalene your_prog.py                             # full profile (outputs to web interface)
python3 -m scalene your_prog.py                  # equivalent alternative

scalene --cli your_prog.py                       # use the command-line only (no web interface)

scalene --cpu your_prog.py                       # only profile CPU
scalene --cpu --gpu your_prog.py                 # only profile CPU and GPU
scalene --cpu --gpu --memory your_prog.py        # profile everything (same as no options)

scalene --reduced-profile your_prog.py           # only profile lines with significant usage
scalene --profile-interval 5.0 your_prog.py      # output a new profile every five seconds

scalene (Scalene options) --- your_prog.py (...) # use --- to tell Scalene to ignore options after that point
scalene --help                                   # lists all options
```

</details>

<details>
<summary>
Using Scalene programmatically in your code:
</summary>

Invoke using `scalene` as above and then:

```Python
from scalene import scalene_profiler

# Turn profiling on
scalene_profiler.start()

# Turn profiling off
scalene_profiler.stop()
```

</details>

<details>
<summary>
Using Scalene to profile only specific functions via <code>@profile</code>:
</summary>

Just preface any functions you want to profile with the `@profile` decorator and run it with Scalene:

```Python
# do not import profile!

@profile
def slow_function():
    import time
    time.sleep(3)
```

</details>

#### Web-based GUI

Scalene has both a CLI and a web-based GUI [(demo here)](http://plasma-umass.org/scalene-gui/).

By default, once Scalene has profiled your program, it will open a
tab in a web browser with an interactive user interface (all processing is done
locally). Hover over bars to see breakdowns of CPU and memory
consumption, and click on underlined column headers to sort the
columns. The generated file `profile.html` is self-contained and can be saved for later use.

[![Scalene web GUI](https://raw.githubusercontent.com/plasma-umass/scalene/master/docs/scalene-gui-example.png)](https://raw.githubusercontent.com/plasma-umass/scalene/master/docs/scalene-gui-example-full.png)


## Scalene Overview

### Scalene talk (PyCon US 2021)

[This talk](https://youtu.be/5iEf-_7mM1k) presented at PyCon 2021 walks through Scalene's advantages and how to use it to debug the performance of an application (and provides some technical details on its internals). We highly recommend watching this video!

[![Scalene presentation at PyCon 2021](https://raw.githubusercontent.com/plasma-umass/scalene/master/docs/images/scalene-video-img.png)](https://youtu.be/5iEf-_7mM1k "Scalene presentation at PyCon 2021")
