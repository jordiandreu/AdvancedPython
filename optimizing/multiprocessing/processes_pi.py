# file: processes_pi.py

"""Calculation of pi with Monte Carlo and multiprocessing.
"""

from __future__ import print_function

import math
try:
    from multiprocessing import Process, Queue                  #1
except ImportError:
    from processing import Process, Queue                       #2
import random
import timeit
import sys


if sys.version_info[0] < 3:
    range = xrange

def count_inside(total):                                        #3
    """Count the hits inside the circle.

    This function will be run multiple times in different
    processes.
    """
    inside_count = 0
    for _ in range(total):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x * x + y * y)
        if dist < 1:
            inside_count += 1
    return inside_count


def calc_pi(total):                                             #4
    """Determine pi _without_ multprocessing as refrence.
    """
    return 4 * count_inside(total) / float(total)


def count_inside_process(queue, total):                         #5
    """Count the hits inside the circle in a seperate process.
    """
    queue.put(count_inside(total))


def calc_pi_processes(total, process_count):                    #6
    """Calculate pi spread of several processses.

    We need to split the task into sub tasks before we can hand
    them to other processes.
    """
    min_n = total // process_count                              #7
    counters = [min_n] * process_count                          #8
    reminder = total % process_count                            #9
    for count in range(reminder):                               #10
        counters[count] += 1                                    #11
    queues_processes = []                                       #12
    for counter in counters:                                    #13
        queue = Queue()                                         #14
        process = Process(target=count_inside_process,
                           args=(queue, counter))               #15
        process.start()                                         #16
        queues_processes.append((queue, process))               #17
    inside_count = sum(queue.get() for queue, _
                       in queues_processes)                     #18
    for _, process in queues_processes:                         #19
        process.join()                                          #20
    return 4 * inside_count / float(total)                      #21

if __name__ == '__main__':

    def test():
        """Check if it works.
        """
        process_count = 3                                       #22
        total = int(1e6)                                        #23
        print('number of tries: %2.0e' % total)                 #24

        start = timeit.default_timer()                          #25
        pi = calc_pi(total)
        one_time = timeit.default_timer() - start
        print('pi:', pi)
        print('run time one process:', one_time)

        start = timeit.default_timer()                          #26
        pi = calc_pi_processes(total, process_count)            #27
        two_time = timeit.default_timer() - start
        print('pi:', pi)
        print('run time %d processes:' % process_count, two_time)

        print('ratio:', one_time / two_time)                     #28
        print('diff:', two_time - one_time)

    test()
