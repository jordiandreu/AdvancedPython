import StringIO


fobj = StringIO.StringIO("""Hello world
    Hallo Welt""")

line1 = fobj.next()

print 'Done'