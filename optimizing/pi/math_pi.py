# file: math_pi.py

"""Variation on `pi_plain` but using `hypot`
from the `math` module.
"""

from __future__ import print_function

import math
import random


def pi_math(total):                                             #1
    """Pi calculation using hypot.
    """
    count_inside = 0
    for _ in range(total):
        x = random.random()
        y = random.random()
        dist = math.hypot(x, y)                                 #2
        if dist < 1:
            count_inside += 1
    return 4.0 * count_inside / total

if __name__ == '__main__':

    import plain_pi
    import measure_time
    pi_plain = plain_pi.pi_plain

    def test():
        """Check if it works.
        """

        names = ['pi_plain', 'pi_math']
        total = int(1e6)
        repeat = 5
        measure_time.measure_run_time(total, names, repeat)

    test()
