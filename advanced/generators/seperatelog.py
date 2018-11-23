"""Use coroutines to sum log file data with different log levels.
"""

import functools
import sys
import time


def init_coroutine(func):
    @functools.wraps(func)
    def init(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return init


def read_forever(fobj, target):
    """Read from a file as long as there are lines.
    Wait for the other process to write more lines.
    Send the lines to `target`.
    """
    while True:
        line = fobj.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@init_coroutine
def filter_comments(target):
    """Filter out all lines starting with #.
    """
    while True:
        line = yield
        if not line.strip().startswith('#'):
            target.send(line)


@init_coroutine
def get_number(targets):
    """Read the number in the line and convert it to an integer.
    Use the level read from the line to choose the to target.
    """
    while True:
        line = yield
        level, number = line.split(':')
        number = int(number)
        targets[level].send(number)

# Consumers for different cases.

@init_coroutine
def fatal():
    """Handle fatal errors."""
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('FATAL    sum: %7d\n' % sum_)


@init_coroutine
def critical():
    """Handle critical errors."""
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('CRITICAL sum: %7d\n' % sum_)


@init_coroutine
def error():
    """Handle normal errors."""
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('ERROR    sum: %7d\n' % sum_)


@init_coroutine
def warn():
    """Handle warnings."""
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('WARN     sum: %7d\n' % sum_)


@init_coroutine
def debug():
    """Handle debug messages."""
    sum_ = 0
    while True:
        value = (yield)
        sum_ += value
        sys.stdout.write('DEBUG    sum: %7d\n' % sum_)


TARGETS = {'CRITICAL': critical(),
           'DEBUG': debug(),
           'ERROR': error(),
           'FATAL': fatal(),
           'WARN': warn()}


def show_sum(file_name='out.txt'):
    """Start start the pipeline.
    """
    # read_forever > filter_comments > get_number > TARGETS
    read_forever(open(file_name), filter_comments(get_number(TARGETS)))


if __name__ == '__main__':
    show_sum(sys.argv[1])
