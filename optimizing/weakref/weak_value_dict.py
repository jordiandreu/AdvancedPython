"""Example of WeakValueDictionary for id to object translation.

Inspired by the Python documentation:
https://docs.python.org/3/library/weakref.html?highlight=weakref#example
"""

import weakref


class IDStore:
    """Storage of objects by ID.
    """

    def __init__(self):
        self._id2obj_dict = weakref.WeakValueDictionary()


    def remember(self, obj):
        """Remember the object in a weak value dictionary.
        """
        oid = id(obj)
        self._id2obj_dict[oid] = obj
        return oid


    def id2obj(self, oid):
        """Retrieve the object by its id.
        """
        return self._id2obj_dict[oid]


class MyClass:
    """Simple example class.
    """
    pass

def test():
    """Simple test.

    Shows that class instance disappears from dictionary when deleted
    but not explicitly removed from the weak value dictionary used to
    store the object.
    """

    id_store = IDStore()

    print('First instance')
    print('===============')
    my_inst = MyClass()
    print('object id:', id_store.remember(my_inst))
    print('Is retrieved object my object?:',
          id_store.id2obj(id(my_inst)) is my_inst)
    print('Show weak value dict:', dict(id_store._id2obj_dict))
    print('delete instance')
    del my_inst
    print('Show weak value dict:', dict(id_store._id2obj_dict))

    print()
    print('Second instance')
    print('===============')
    my_inst = MyClass()  # catch freed id to avoid the same id in store
    my_inst = MyClass()
    print('object id:', id_store.remember(my_inst))
    print('Is retrieved object my object?:',
          id_store.id2obj(id(my_inst)) is my_inst)
    print('Show weak value dict:', dict(id_store._id2obj_dict))
    print('delete instance')
    del my_inst
    print('Show weak value dict:', dict(id_store._id2obj_dict))


if __name__ == '__main__':

    test()
