# file: plain_pi.py

"""Calculating pi with Monte Carlo.
"""

from __future__ import print_function

import math                                                     #1
import random
import sys

# make `import measure_time` work
sys.path.append('../measuring')
import measure_time                                             #2


if sys.version_info[0] < 3:
    range = xrange

def pi_plain(total):                                            #3
    """Calculate pi with `total` hits.
    """
    count_inside = 0                                            #4
    for _ in range(total):                                     #5
        x = random.random()                                     #6
        y = random.random()                                     #7
        dist = math.sqrt(x * x + y * y)                         #8
        if dist < 1:
            count_inside += 1                                   #9
    return 4.0 * count_inside / total                           #10

if __name__ == '__main__':                                      #11

    def test():
        """Check if it works.
        """
        n = 1e6
        print('pi:', pi_plain(int(n)))                          #12
        names = ['pi_plain']                                    #13
        total = int(n)                                          #14
        repeat = 3                                              #15
        measure_time.measure_run_time(total, names, repeat)     #16

    test()
