from distutils.sysconfig import get_makefile_filename as m
from os.path import isfile 
import sys 
sys.exit(not isfile(m()))
