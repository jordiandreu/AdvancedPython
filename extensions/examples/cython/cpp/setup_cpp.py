# file: setup_cpp.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name = 'cython_cpp',
  ext_modules=[
    Extension('cython_cpp',
              sources=['cython_cpp.pyx', 'cxx/cpp_pi.cpp'],
              depends=['cython_cpp.pxd', 'cxx/cpp_pi.h'],
              include_dirs=['cxx'],
              language='c++')
    ],
  cmdclass = {'build_ext': build_ext}
)