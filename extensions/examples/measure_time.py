# file: measure_time.py

from timeit import Timer                                    #1

def measureRunTime(n, names, number=1):                     #2
   
    def timeitRunner(name):                                 #3
        t = Timer('%s(n)' %name,
                  'from __main__ import %s\nn=%d'
                  %(name, n))                               #4
        return t.timeit(number), name                       #5

    results = []                                            #6
    for name in  names:
        results.append(timeitRunner(name))                  #7
    results.sort()                                          #8
    length = max(len(name) for name in (names))             #9
    format1 = '%%-%ds' %length
    header = (format1 + '%s%10s') %('Function',
                                    'Time'.center(11), 'Ratio')
    print
    print header
    print '=' * len(header)
    for result in results:
        ratio = result[0] / results[0][0]
        print (format1 +  '%9.4f s%10.2f') %(result[1],
                                             result[0], ratio)
        
