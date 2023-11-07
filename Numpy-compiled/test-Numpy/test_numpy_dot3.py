#!/usr/bin/env python
import numpy
#from numpy.distutils.system_info import get_info
import sys
import timeit
import os 

print("version: %s" % numpy.__version__)
print("maxint:  %i\n" % sys.maxsize)

#info = get_info('blas_opt')
#print('BLAS info:')
#for kk, vv in info.items():
#    print(' * ' + kk + ' ' + str(vv))

size=int(sys.argv[1])
#size= int(input('Insert the size of the matrix to test:'))

setup = "import numpy; x = numpy.random.random(({}, {}))".format(size,size)
count = 10

t = timeit.Timer("numpy.dot(x, x.T)", setup=setup)
print("\ndot: %f sec" % (t.timeit(count) / count))
