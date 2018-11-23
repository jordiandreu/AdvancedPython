# file: setup_c.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name = 'cython_c',
  ext_modules=[
    Extension('mc_pi_cython_c', ['mc_pi_cython_c.pyx', 'cpi.c']) #1
    ],
  cmdclass = {'build_ext': build_ext}
)