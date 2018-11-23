# file: cython_cpp_property.pyx


cdef class PyPiMaker:
    """Wrap the C++ class.
    """
    cdef PiMaker *thisptr
    cdef bint has_pi
    def __cinit__(self):
        self.thisptr = new PiMaker()
        self.has_pi = 0
    def __dealloc__(self):
        del self.thisptr
    property n:
        def __get__(self):
            # return self.thisptr.n
            # This does NOT compile because ``n`` is private.
            #raise AttributeError("Can't access a private attribute.")
            return self.thisptr.get_n()
        def __set__(self, n):
            self.thisptr.set_n(n)
            self.has_pi = 1
    property pi:
        def __get__(self):
            if self.has_pi:
                return self.thisptr.get_pi()
            else:
                raise ArithmeticError('Pi has not been calculated yet.')

