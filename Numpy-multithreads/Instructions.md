# Numpy multi-threaded

NumPy does not depend on any other Python packages. However, it does depend on accelerated linear algebra libraries - typically Intel MKL,OpenBLAS  or LAPACK. Accordingly to the selected automatic method to install numpy one of these libraries is automatically included in the installation phase. Power users may still want to know the details, because the used BLAS can affect performance, behavior and size on disk.

For Numpy version>1.21 NumPy wheels on PyPI, which is what pip installs, are built with OpenBLAS. The OpenBLAS libraries are included in the wheel. This makes the wheel larger, and if a user installs (for example) SciPy as well, they will now have two copies of OpenBLAS on disk.

In the conda defaults channel, NumPy is built against Intel MKL. MKL is a separate package that will be installed in the users’ environment when they install NumPy.

In the conda-forge channel, NumPy is built against a dummy “BLAS” package. When a user installs NumPy from conda-forge, that BLAS package then gets installed together with the actual library - this defaults to OpenBLAS, but it can also be MKL (from the defaults channel), or even BLIS or reference BLAS.

The MKL package is a lot larger than OpenBLAS, it’s about 700 MB on disk while OpenBLAS is about 30 MB. However, for INTEL CPUs it is typically a little faster and more robust than OpenBLAS.

Besides install sizes, performance and robustness, there are two more things to consider:
 - Intel MKL is not open source. For normal use this is not a problem, but if a user needs to redistribute an application built with NumPy, this could be an issue.
 - Both MKL and OpenBLAS will use multi-threading for function calls like np.dot, with the number of threads being determined by both a build-time option and an environment variable. Often all CPU cores will be used. This is sometimes unexpected for users; NumPy itself doesn’t auto-parallelize any function calls. It typically yields better performance, but can also be harmful - for example when using another level of parallelization with Dask, scikit-learn or multiprocessing.



Today we are gonna install Numpy following three different approaches:
- installing OpenBLAS from source, with OPENMP support, and compiling the Numpy library (downloaded from the official Github repo) linking the library against the installed multi-threaded version of OpenBLAS 
- using pip in venv to install Numpy
- using conda to install Numpy from the Conda default channel

To install OpenBLAS let's take a look at file Installing_OpenBLAS.md

Once installed OpenBLAS we can proceed with Numpy installation from source.
Everything reported below is valid for a Python version >=3.8 and <=3.10.


# Installing Numpy from source in a dedicated virtual environment

First, we need to create a dedicated virtual environment (and we will use venv for this)
$ python -m venv Penv/CompiledNumpy

The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories.

We need to activate the virtual env
$ source Penv/CompiledNumpy/bin/activate

and we can check we are in the correct env using
$ which python


Now we clone locally Numpy official Github repo:

$ git clone git@github.com:numpy/numpy.git 

We update the git submodule to be safe
$ git submodule update --init

We move to the latest numpy version supporting Python 3.8
 
$ git checkout v1.24.1 

To install numpy we need both python3 and python3-dev
To see if python3-dev is installed you can use the code

launching command:
python3 check-py-dev.py && echo "Ok" || echo "Error: Python header files NOT found"


To install the missing libraries needed to install numpy we launch the command

$ python -m pip install -r test_requirements.txt

$ cp site.cfg.example site.cfg

Now we set the environmental variables needed
export PYTHON_VERSION="3.8.10"
export CYTHON_VERSION="0.29.36"

we need to copy the configuration example file to the file that we will use to build numpy
$ cp site.cfg.example site.cfg

We need to modify the new configuration files (we will use the editor vim for this) 

$ apt-get install vim

$ vim site.cfg

We need to uncomment the lines under OPENBLAS section, from line n. 106 to 111

and write the directory with headers and shared libraries relating to OPENBLAS:
"""
 [openblas]
 libraries = openblas
 library_dirs = /afs/ictp.it/home/s/sdigioia/installed-OpenBLAS/lib
 include_dirs = /afs/ictp.it/home/s/sdigioia/installed-OpenBLAS/include
 runtime_library_dirs = /afs/ictp.it/home/s/sdigioia/installed-OpenBLAS/lib

"""
NOTE: you should change the user name from mine (sdigioia) to yours!!!! 

Now, we can build the numpy library specifying to use the Fortran compiler
$ NPY_LAPACK_ORDER=openblas,MKL,ATLAS python setup.py build --fcompiler=gnu95

Then, we can install the Numpy library with the command
$ pip install .

Now we can deactivate this environment:
$ deactivate

# Installing Numpy with pip install from the official wheels

To install Numpy with pip from the official wheel we need only a one-line command.
We will create a separate virtual environment with venv to test this installattion.

$ python -m venv Penv/StandardNumpy

To enter the new virtual environment we run 

$ source Penv/StandardNumpy/bin/activate

and we can directly install Numpy, because in the pip wheel there will be all the requirements of this libraries.

$ pip install numpy==1.24.1

To test this installation we use the get_info.py code in the subdir test-numpy

$python get_info.py

Now we can deactivate the virtual enviroment
$ deactivate

# Installing Numpy with conda 

First we need to install Anaconda on our local machine

To install Anaconda we need to check if requirements are installed and install if not:
apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

We move to scratch area 
$ cd /scratch/sdigioia

Then we can download the bash script to install the latest Anaconda release on Linux
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh

We change the file permits to run it as an executable 
$ chmod +x Anaconda3-2023.09-0-Linux-x86_64.sh

and we run the executable:
$./Anaconda3-2023.09-0-Linux-x86_64.sh (or also bash Anaconda3-2023.09-0-Linux-x86_64.sh)

then we can launch the installer, and once finished we run:
$ conda create -p /scratch/sdigioia/conda-env/CondaNumpy -c conda-forge --override-channels python=3.9 numpy=1.24.1 mkl=2019.* blas=*=*mkl

All the steps showed in this tutorial were tested on the pc "hpc6g4-dnrd-5" in the Lab.
