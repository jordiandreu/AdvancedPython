# coding: utf-8
import sys

class MyContext:
    
    def __enter__(self):
        self.fobj = open('stdout.txt', 'w')
        self._stdout = sys.stdout
        sys.stdout = self.fobj
    
    # signature: exception type and value, and traceback
    def __exit__(self, ex_t, ex_v, tb):
        sys.stdout = self._stdout
        self.fobj.close()
        
with MyContext() as ctx:
    print('inside the file')
print('in command line')
