#!/usr/bin/env python
import numpy
from numpy.distutils.system_info import get_info
import sys
import timeit

print("Numpy version: %s" % numpy.__version__)
print("maxint:  %i\n" % sys.maxsize)
info = get_info('blas_opt')
print('BLAS info:')
for kk, vv in info.items():
    print(' * ' + kk + ' ' + str(vv))


