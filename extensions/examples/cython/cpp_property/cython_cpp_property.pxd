# file: cython_cpp.pxd

# declare the interface
cdef extern from 'cpp_pi.h':   #1
    cdef cppclass PiMaker:     #2
        PiMaker()              #3
        double get_n()           #4
        void set_n(int n)        #5
        double get_pi()        #6
