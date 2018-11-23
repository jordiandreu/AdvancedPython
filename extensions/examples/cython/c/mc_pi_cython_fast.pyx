# file: mc_pi_cython_fast.pyx

import time

cdef extern from "math.h":          #1
    double sqrt(double x)           #2

cdef extern from "stdlib.h":        #3
    int rand()                      #4
    int RAND_MAX                    #5
    void srand (unsigned int SEED)  #6


def pi_cython(int n):
    """Use static typing, C functions
    and cython loop.
    """
    cdef int count_inside, count    #7
    cdef float x, y, rand_max       #8
    count_inside = 0
    srand(time.time())              #9
    rand_max = float(RAND_MAX)      #10
    for count in range(n):          #11
        x = rand() / rand_max       #12
        y = rand() / rand_max
        d = sqrt(x*x + y*y)         #13
        if d < 1:                   #14
            count_inside = count_inside + 1
    return 4.0 * count_inside / n

