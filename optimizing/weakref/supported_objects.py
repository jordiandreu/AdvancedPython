"""Simple test for weakly reference-able objects.
"""

from collections import defaultdict
import weakref
import sys

class MyClass:
    """Empty class.
    """
    pass


def test(objects):
    """Show if objects can be weakly referenced.
    """
    for obj in objects:
        try:
            weakref.ref(obj)
            print('works for', type(obj))
        except TypeError:
            print("doesn't work for", type(obj))

if __name__ == '__main__':

    objects = [MyClass(), set(), frozenset(), sys, defaultdict(), [], {}, (),
               'a', 2, 3.5,  object(), range(10), zip()]
    test(objects)