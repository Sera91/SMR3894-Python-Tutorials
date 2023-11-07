Today we are gonna install Openblas on our laptops and after that we are gonna compile the Numpy library linking the multi-threaded version of the [openBLAS](https://www.openblas.it) library .

Different releases of the openBLAS library are available on Github at:
https://github.com/OpenMathLib/OpenBLAS/releases

We are going to install the latest stable release: 0.3.24

We can use the following command on the terminal:
wget https://github.com/OpenMathLib/OpenBLAS/releases/download/v0.3.21/OpenBLAS-0.3.21.tar.gz

We untar the compressed file
and we enter the directory 
$ cd OpenBLAS && make FC=gfortran
then we create a folder to where we want to install the BLAS library
$ mkdir installed-BLAS
and we proceed with installation
$ make install PREFIX=$HOME/installed-BLAS install


Then to avoid to redefine the environmental variable for linking library every time we need to recompile numpy we add to our .bashrc
this line:
$ export LD_LIBRARY_PATH=/opt/OpenBLAS/lib:$LD_LIBRARY_PATH 


