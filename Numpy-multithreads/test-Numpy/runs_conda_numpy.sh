#!/bin/bash
  
conda activate /scratch/sdigioia/conda-env/CondaNumpy

#which python

array=(1000 2000 4000)

python get_info.py

for i in "${array[@]}"
do
 OMP_NUM_THREADS=1
 echo "N_threads=1"
 OMP_NUM_THREADS=1 python test_numpy_dot3.py $i
 echo "N_threads=2"
 OMP_NUM_THREADS=2 python test_numpy_dot3.py $i
 echo "N_threads=4"
 OMP_NUM_THREADS=4 python test_numpy_dot3.py $i
 echo "N_threads=8"
 OMP_NUM_THREADS=8 python test_numpy_dot3.py $i
done

deactivate



 
