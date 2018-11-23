# coding: utf-8
import sys
import contextlib

@contextlib.contextmanager
def mycontext():
    
    try:
        fobj = open('stdout.txt', 'w')
        stdout = sys.stdout
        sys.stdout = fobj
        yield
    
    finally:
        sys.stdout = stdout
        fobj.close()
        
with mycontext() as ctx:
    print('inside the file')
print('in command line')
