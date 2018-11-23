# file: setup_fast.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name = 'cython_fast',
  ext_modules=[
    Extension('mc_pi_cython_fast', ['mc_pi_cython_fast.pyx'])
    ],
  cmdclass = {'build_ext': build_ext}
)