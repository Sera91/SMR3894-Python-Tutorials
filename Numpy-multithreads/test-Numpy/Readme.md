In this folder you fing the python scripts that we will use to test
the different version of numpy installed.

First we consider the numpy installed from source, and linked with OpenBLAS,
and we can execute the Bash script "runs_compiled_numpy.sh" to measure
different runtimes of the dot product between two squared matrices,
for different configurations in terms of number of threads and number of
elements in the matrix.

Then, we move to consider the Numpy installed from the official wheel,
inside the Python virtual environment StandardNumpy

Finally, we consider the Numpy based on the MKL libraries installed inside the conda environment


