# python tutorial
'''
comments
'''
print "let's go"
print "===================================="
print "abs(-5) absolute value of a number, gives %s, error if not number" % abs(-5)
print "===================================="
print "all(x) is true if all x, which is a iterable, is true"
x = [1,2,3,4,5,6,7,8]
print all(x)
x = [1,2,3,4,5,6,7,0]
print all(x)
print "===================================="
print "any(x) is true if any x, which is a iterable, is true"
x = [1,2,3,4,5,6,7,8]
print any(x)
x = []
print any(x)

print "===================================="
print "bin(4) gives %s , a binary string and is type %s" % (bin(4), type(bin(4)))
print "===================================="

print "===================================="


x = "abcdefgh"
print x
print '\n'.join(dir(x))

x = 1
print bool(x)

x = bytearray(2)
print x
print dir(x)
print type(x)
print type(x[0])
print x[0]