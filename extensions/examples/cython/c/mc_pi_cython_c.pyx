# file: mc_pi_cython_c.pyx

cdef extern from "cpi.h":       #1
    double piC(int n)

def pi_cython(int n):           #2
    """Just call the C functon.
    """
    return piC(n)