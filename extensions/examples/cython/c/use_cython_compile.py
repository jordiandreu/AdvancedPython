# file: use_cython_compile.py

import cython

@cython.compile
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(2, 3))