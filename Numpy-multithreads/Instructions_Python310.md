## 1. Installing Dependencies 
The following dependencies are required (note that all code blocks in these notes refer to commands executed from a standard terminal, unless otherwise noted):

```
sudo apt update
sudo apt install pkg-config  build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget git
sudo apt install libsqlite3-dev libbz2-dev uuid-dev lzma-dev libgdm-dev gfortran meson
```

## 2. Compiling Python
Python source for all released versions can be downloaded from  https://www.python.org/downloads/source/https://www.python.org/downloads/source/ 
Here, we will use version 3.10.2. Specifically, we downloaded file Python-3.10.2.tgz to our Downloads folder.  Then, in a fresh terminal session:

```
cd ~Downloads
tar xvzf Python-3.10.2.tgz
cd Python-3.10.2/
```

As per the README.rst file, we follow the standard `make` procedure, setting a global install `prefix` at the `configure` step to ensure that we do not overwrite system-installed binaries, and toggling on all available optimizations:

```
./configure --prefix=/opt/local --enable-optimizations=yes
make
make test
sudo make install
```


All tests pass successfully, and a `python3` binary is created in `/opt/local/bin`.  For convenience, we can create symbolic links to some of the binaries:

```
cd /opt/local/bin/
sudo ln -s pip3 pip
sudo ln -s python3 python
```

We can also add `/opt/local/bin` to our system `PATH` so that the new binaries are automatically found without having to use the full paths. We do so by executing:

```
export PATH=/opt/local/bin:$PATH
```

We can make this change permanent by adding the same line to the end of our `~/.bashrc` file (assuming that we're running a bash shell, which is Ubuntu's default). 

In order to test the performance, we can use the `pyperformance` package (`pip install pyperformance`). Comparing two different python binaries compiled with an without the `enable-optimizations` flag shows improvements between 10 and 30% in all test categories with the optimizations.

## 3. Compiling OpenBLAS

We can grab OpenBLAS from its GitHub repository.  We'll want to checkout the latest stable branch from its tag (in this example, v0.3.24):

```
git clone https://github.com/OpenMathLib/OpenBLAS
cd OpenBLAS
git tag
git checkout -b v0.3.24 tags/v0.3.24 
```

OpenBlas doesn't have a configure step, and will (by default) install to `/opt/OpenBLAS`.  All we need to do is:

```
make
sudo make install
```

## 4. Compiling Numpy

Just as with OpenBlas, we grab Numpy from its repository and create a branch from the latest stable release tag (in this case 1.26.0).  Since Numpy utilizes submodules, we also need to synchronize those with the tagged versions:

```
git clone --recurse-submodules https://github.com/numpy/numpy.git
git checkout -b v1.26.0 tags/v1.26.0
git submodule update --init
```

We can install the build requirements under the current user, or system-wide.  In the latter case we do:

```
pip install -r build_requirements.txt
pip install -r test_requirements.txt
```

In order to utilize our OpenBLAS build, we need to point at the pkgconfig file.  We do so by setting the `PKG_CONFIG_PATH` environemtn variable:

```
export PKG_CONFIG_PATH=/opt/OpenBLAS/lib/pkgconfig/
```

Finally, as per the Numpy README, we can then perform a local, editable install by executing:

```
/opt/local/bin/pip install -e . --no-build-isolation
```

