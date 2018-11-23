# file: mc_pi_cython_nochange.pyx

import math
import random

def pi_cython(n):
    """Still pure Python.
    """
    count_inside = 0
    for count in range(n):
        x = random.random()
        y = random.random()
        d = math.sqrt(x*x + y*y)
        if d < 1:
            count_inside = count_inside + 1
    return 4.0 * count_inside / n