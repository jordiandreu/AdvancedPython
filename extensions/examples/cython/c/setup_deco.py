# file: setup_deco.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name = 'cython_deco',
  ext_modules=[
    Extension('mc_pi_cython_deco', ['mc_pi_cython_deco.py'])
    ],
  cmdclass = {'build_ext': build_ext}
)
