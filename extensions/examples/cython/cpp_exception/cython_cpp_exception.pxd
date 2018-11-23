# file: cython_cpp.pxd

# declare the interace
cdef extern from 'cpp_pi.h':
    cdef cppclass PiMaker:
        PiMaker()
        double get()
        void set(int n) except +