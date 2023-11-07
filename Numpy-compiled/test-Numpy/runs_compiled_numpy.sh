#!/bin/bash
  
source $HOME/Penv/CompiledNumpy/bin/activate

array=(1000 2000 4000)

python get_info.py

for i in "${array[@]}"
do
 OMP_NUM_THREADS=1
 OPENBLAS_NUM_THREADS=1 python test_numpy_dot3.py $i
 OPENBLAS_NUM_THREADS=2 python test_numpy_dot3.py $i
 OPENBLAS_NUM_THREADS=4 python test_numpy_dot3.py $i
 OPENBLAS_NUM_THREADS=8 python test_numpy_dot3.py $i
done

deactivate



 
