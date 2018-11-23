# file: cython_cpp.pyx


cdef class PyPiMaker:                         #1
    """Wrap the C++ class.
    """
    cdef PiMaker *thisptr                     #2
    def __cinit__(self):                      #3
        self.thisptr = new PiMaker()          #4
    def __dealloc__(self):                    #5
        del self.thisptr                      #6
    def set_n(self, n):
        self.thisptr.set_n(n)                   #7
    def get_n(self):
        return self.thisptr.get_n()             #8
    def get_pi(self):
        return self.thisptr.get_pi()             #8
