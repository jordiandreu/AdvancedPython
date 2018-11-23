# file: setup_nochange.py

from distutils.core import setup            #1
from distutils.extension import Extension   #2
from Cython.Distutils import build_ext      #3

setup(name = 'cython_no_change',            #4
      ext_modules=[                         #5
      Extension('mc_pi_cython_nochange',    #6
      ['mc_pi_cython_nochange.pyx'])],      #7
      cmdclass = {'build_ext': build_ext})  #8