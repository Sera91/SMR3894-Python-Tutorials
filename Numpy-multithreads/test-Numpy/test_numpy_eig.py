import sys
from numpy.random import rand
from numpy.linalg import eig
import time
# size of arrays
n = int(sys.argv[1])

# create an array of random values
data = rand(n, n)

t1=time.process_time()
# decomposition
w, v = eig(data)
t_eig=time.process_time() - t1

print("Eig function call took:", t_eig)
