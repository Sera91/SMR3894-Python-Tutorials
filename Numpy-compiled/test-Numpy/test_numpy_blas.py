import numpy
from numpy.distutils.system_info import get_info
import sys
import timeit


print("Numpy version: %s" % numpy.__version__)

info = get_info('blas_opt')
#printing BLAS infos
print(info)
