# file: multi.py

"""Using Numba with threads.

Needs to have rather arrays to get faster than with threads.
"""


from multiprocessing.pool import ThreadPool

import numba


@numba.jit(nopython=True, nogil=True)
def sum_numbers(array):
    """Sum numbers in 1d array.
    """
    sum_ = 0.0
    for n in range(array.shape[0]):
        sum_ += array[n]
    return sum_


def sum_multi(arr):
    """Sum numbers in 1d array using two threads.
    """
    pool = ThreadPool(processes=2)
    bounds = [(0, arr.size // 2), (arr.size // 2, arr.size)]
    threads = [pool.apply_async(sum_numbers, (arr[start:end],))
               for start, end in bounds]
    return sum(thread.get() for thread in threads)


if __name__ == '__main__':

    def test():
        """As simple test with some timing.
        """
        import timeit

        import numpy as np

        arr = np.arange(int(1e8))
        assert sum_numbers(arr) == sum_multi(arr)

        number = 10
        namespace = globals().copy()
        namespace.update(locals())
        time_numbers = timeit.timeit('sum_numbers(arr)', number=number,
                                     globals=namespace)
        time_multi = timeit.timeit('sum_multi(arr)', number=number,
                                   globals=namespace)
        print('time one thread  :', time_numbers)
        print('time two threads:', time_multi)
        print('ratio:', time_numbers / time_multi)

    test()
