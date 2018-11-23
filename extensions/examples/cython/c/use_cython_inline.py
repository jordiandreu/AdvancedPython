# file: use_cython_inline.py

import cython


def add(a, b):
    return cython.inline('a + b')


if __name__ == '__main__':
    print(add(2, 3))