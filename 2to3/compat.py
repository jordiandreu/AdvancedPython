# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys

__all__ = []

if sys.version_info.major < 3:
    input = raw_input
    range = xrange
    from io import open
    from itertools import izip as zip, imap as map, ifilter as filter
    __all__ = ['input', 'filter', 'map', 'open', 'range', 'zip']
else:
    import builtins
    input = builtins.input
    filter = builtins.filter
    map = builtins.map
    open = builtins.open
    range = builtins.range
    zip = builtins.zip

