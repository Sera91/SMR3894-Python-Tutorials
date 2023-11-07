Today we are gonna install Openblas on our laptops and after that we are gonna compile the Numpy library linking the multi-threaded version of the [openBLAS](https://www.openblas.it) library .

Different releases of the openBLAS library are available on Github at:
https://github.com/OpenMathLib/OpenBLAS/releases

We are going to install the latest stable release: 0.3.24

#Downloading OpenBLAS selected version

##Option A: download compressed source code
We can download the compressed source code using the following command on the terminal:
$ wget https://github.com/OpenMathLib/OpenBLAS/releases/download/v0.3.24/OpenBLAS-0.3.24.tar.gz

We need to untar the compressed file
$ untar -xvzf OpenBLAS-.gz

##Option B: cloning locally the official Git repo of OpenBLAS 

If we have git installed, we can also clone the OpenBLAS project with Git, to get updates easily
$ git clone https://github.com/xianyi/OpenBLAS.git

After extracting OpenBLAS or git cloning the OpenBLAS repo,
we create in our HOME the folder to which we want to install this library:
$ mkdir installed-OpenBLAS 

#Installing OpenBLAS and setting environment

We need to enter the OpenBLAS directory and we select the Fortran compiler
$ cd OpenBLAS 

and we compile OpenBLAS using the Fortran compiler gfortran:
$make FC=gfortran

NOTE: This will take some min....

Then, we proceed with installation
$ make PREFIX=$HOME/installed-OpenBLAS install


After checking that the installation has concluded successfully,  we add to our .bashrc
this line:
$ export LD_LIBRARY_PATH=$HOME/installed-OpenBLAS/lib:$LD_LIBRARY_PATH 


#Installing Numpy in a dedicated virtual environment

First, we need to create a dedicated virtual environment (and we will use venv for this)
$ python -m venv /path/to/new/virtual/environment 
for Python <3.6 we use pyvenv

The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories.

We need to activate the virtual env
$ source Penv/Seraenv/bin/activate

and we can check we are in the correct env using
$ which python


Now we clone locally Numpy official Github repo:

$ git clone 

We move to the latest numpy version supporting Python 3.8
 
$ git checkout v1.24.1 

$ python -m pip install -r test_requirements.txt

$ cp site.cfg.example site.cfg

export PYTHON_VERSION="3.8.10"
export CYTHON_VERSION="0.29.36"

python setup.py build --fcompiler=gnu95

LD_PRELOAD=/afs/ictp.it/home/s/sdigioia/installed-OpenBLAS/lib/libopenblas.so.0 python setup.py config

To install numpy we need both python3 and python3-dev
To see if python3-dev is installed you can use the code

launching command:
python3 check-py-dev.py && echo "Ok" || echo "Error: Python header files NOT found"

We can build the numpy library specifying to use the Fortran compiler
NPY_LAPACK_ORDER=openblas,MKL,ATLAS python setup.py build --fcompiler=gnu95

We can install the 
pip install .



