"""Create a weak reference with a list.
"""

import weakref


class MyList(list):
    """My list is just inherits from `list`.
    Need this because built-in list does not work with weak refs.
    """
    pass


def test():
    """Simple test.
    """
    my_list = MyList([1, 2, 3])

    print('List:', my_list)
    print('Weak reference count:', weakref.getweakrefcount(my_list))
    weak_list = weakref.ref(my_list)
    print('Creating a weak reference.')
    print('Weak reference count:', weakref.getweakrefcount(my_list))
    print('Calling the weakref object', weak_list())
    print('Deleting the original list.')
    del my_list
    print('Weak reference count:', weak_list())


if __name__ == '__main__':

    test()
