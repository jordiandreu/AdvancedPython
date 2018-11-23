# file: cython_cpp.pyx


cdef class PyPiMaker:                         #1
    """Wrap the C++ class.
    """
    cdef PiMaker *thisptr                     #2
    def __cinit__(self):                      #3
        self.thisptr = new PiMaker()          #4
    def __dealloc__(self):                    #5
        del self.thisptr                      #6
    def set(self, n):
        self.thisptr.set(n)                   #7
    def get(self):
        return self.thisptr.get()             #8