# coding: utf-8
import sys

__all__ = []

if sys.version_info.major < 3:
    round = my_round
    range = xrange
    from io import open
    __all__ = ['round', 'range', 'open']
