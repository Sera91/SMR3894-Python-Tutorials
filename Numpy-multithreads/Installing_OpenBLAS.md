# Installing a specific version of OpenBLAS from source

The multi-threaded version of [openBLAS](https://www.openblas.it) library 
is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

# What is BLAS? Why is it important?
BLAS stands for Basic Linear Algebra Subprograms. BLAS provides standard interfaces for linear algebra, including BLAS1 (vector-vector operations), BLAS2 (matrix-vector operations), and BLAS3 (matrix-matrix operations). In general, BLAS is the computational kernel ("the bottom of the food chain") in linear algebra or scientific applications. Thus, if BLAS implementation is highly optimized, the whole application can get substantial benefit.


Different releases of the openBLAS library are available on Github at:
https://github.com/OpenMathLib/OpenBLAS/releases

The current release of OpenBLAS is 0.3.24 version created Sep 3, 2023. You can check the changelog file at:

You can read the USER manual at:
https://github.com/OpenMathLib/OpenBLAS/wiki/User-Manual


We are going to install the latest stable release: 0.3.24

#STEP 1) Downloading OpenBLAS selected version

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

#STEP 2) Installing OpenBLAS
We need to enter the OpenBLAS directory and we select the Fortran compiler
$ cd OpenBLAS 

and we compile OpenBLAS using the Fortran compiler gfortran:
$make clean
$make FC=gfortran USE_OPENMP=1

NOTE: This will take some min....

Then, we proceed with installation
$ make PREFIX=$HOME/installed-OpenBLAS install


After checking that the installation has concluded successfully,  we add to our .bashrc
this line:
$ export LD_LIBRARY_PATH=$HOME/installed-OpenBLAS/lib:$LD_LIBRARY_PATH 

