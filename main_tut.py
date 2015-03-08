# python tutorial
'''
comments -- the basics -- before we get fancy we should use
1) decent algorithms
2) builit ins
3) well documented and tested libraries
4) Reinvent the wheel
'''


print "===================================="
print "abs()"
print "abs(-5) absolute value of a number, gives %s, error if not number" % abs(-5)
print "===================================="
print "all()"
print "all(x) is true if all x, which is a iterable, is true"
x = [1,2,3,4,5,6,7,8]
print all(x)
x = [1,2,3,4,5,6,7,0]
print all(x)
print "===================================="
print "any()"
print "any(x) is true if any x, which is a iterable, is true"
x = [1,2,3,4,5,6,7,8]
print any(x)
x = []
print any(x)
print "===================================="
print "basestring()"
print "This abstract type is the superclass for str and unicode. It cannot be called or instantiated"
print "===================================="
print "bin()"
print "Convert an integer number to a binary string"
print "bin(4) gives %s , a binary string and is type %s" % (bin(4), type(bin(4)))
print "===================================="
print "bool()"
print "Return a Boolean value, i.e. one of True or False"
print "bool(0) gives %s, and bool(1) gives %s" % ( bool(0), bool(1))
print "===================================="
print "bytearray()"
print "Return a new array of bytes."
print "bytearray('test') gives %s" % bytearray('test')
print "===================================="
print "callable()"
print "Return True if the passed object argument appears callable, False if not"
print "callable('test') returns %s" % callable('test')
print "===================================="
print "chr()"
print "Return a string of one character whose ASCII code is the integer i."
print "chr(97) evaluates to >%s<" % chr(97)
print "===================================="
print "classmethod()"
print "===================================="
print "cmp(x, y)"
print "Compare the two objects x and y and return an integer according to the outcome."
print "The return value is negative if x < y, zero if x == y and strictly positive if x > y."
print "cmp(10,0) is %s" % cmp(10,0)
print "===================================="
print "compile()"
print "compile is the low level way to dynamically run up code"
print "Compile the source into a code or AST object. Code objects can be executed by an exec statement or evaluated by a call to eval()."
zzz=compile("ppp=99",'<string>','exec')
exec zzz
print "zzz=compile('ppp=99','<string>','exec') , then executing exec zzz, then printing ppp gives %s" % ppp
print "===================================="
print "complex([real[, imag]])"
print "Return a complex number with the value real + imag*j or convert a string or number to a complex number. "
print "complex(10,-5) returns %s" % complex(10,-5)
print "===================================="
print "delattr(object, name)"
print "The function deletes the named attribute of the object, provided the object allows it. "
print "===================================="
print "dict()"
print "creates a dict, with either an mapping and iterable or kwargs"
print "dict(one=1, two=2, three=3) prints %s" % dict(one=1, two=2, three=3)
print "===================================="
print "dir()"
print "Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object."
print "So, dir() is %s" % dir()
print "===================================="
print "divmod()"
print "Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using long division"
print "divmod(7,2) gives %s" % str(divmod(7,2))
print "===================================="
print "enumerate()"
print "with a passed iterable, creates an iter object that return a tuple with the pos,val"
print "enumerate([1,2,3,4,5]).next() gives %s" % str(enumerate([1,2,3,4,5]).next())
print "===================================="
print "eval()"
print "The return value is the result of the evaluated expression (string)"
print "eval(7+2) is %s" % eval('7 + 2')
print "===================================="
print "execfile()"
print "This function is similar to the exec statement, but parses a file instead of a string."
print "===================================="
print "file()"
print "When opening a file, it's preferable to use open() instead of invoking this constructor directly."
print "===================================="
print "filter()"
print "===================================="
print "float()"
print "Return a floating point number constructed from a number or string x"
print "float(4.5) is %s and has type of %s" % (float(4.5), type(float(4.5)) )
print "===================================="
print "format()"
print "===================================="
print "frozenset()"
print "===================================="
print "getattr()"
print "===================================="
print "globals()"
print "===================================="
print "hasattr()"
print "===================================="
print "hash()"
print "===================================="
print "help()"
print "===================================="
print "hex()"
print "===================================="
print "id()"
print "Return the 'identity' of an object."
print "id(44) is %s" % id(44)
print "===================================="
print "input()"
print "===================================="
print "int()"
print "Return an integer object constructed from a number or string x"
print "int(4.5) is %s and has type of %s" % (int(4.5), type(int(4.5)) )
print "===================================="
print "isinstance()"
print "===================================="
print "issubclass()"
print "===================================="
print "iter()"
print "Return an iterator object. Object must be a kind of sequence"
print "iter([1,2,3,4,5]) gives %s" % iter([1,2,3,4,5])
print "===================================="
print "len()"
print "Return the length (the number of items) of an object."
print "len([1,2,3,4]) is %s" % len([1,2,3,4])
print "===================================="
print "list(iterable)"
print "Return a list whose items are the same and in the same order as iterable's items."
print "list('abc') is %s" % list('abc')
print "===================================="
print "locals()"
print "Update and return a dictionary representing the current local symbol table."
print "locals() returns %s" % locals()
print "===================================="
print "long()"
print "===================================="
print "map()"
print "===================================="
print "max()"
print "Return the max amount of an iterable, or of a number of arguments"
print "max([55,33,234,5,1,-2]) is %s" % max([55,33,234,5,1,-2])
print "===================================="
print "memoryview()"
print "Return a 'memory view' object created from the given argument."
print "not used much"
print "===================================="
print "min()"
print "Return the smallest item in an iterable or the smallest of two or more arguments."
print "min([55,7,33,24,5,6,2) is %s " % min([55,7,33,24,5,6,2])
print "===================================="
print "next()"
print "Retrieve the next item from the iterator by calling its next() method. "
print "next(iter([22,33,44,55])) is %s" % next(iter([22,33,44,55]))
print "===================================="
print "object()"
print "===================================="
print "oct()"
print "Convert an integer number (of any size) to an octal string."
print "oct(66) gives %s" % oct(66)
print "===================================="
print "open()"
print "Open a file (passed in as a string), returning an object of the file type"
print "===================================="
print "ord()"
print "Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object"
print "ord('a') is %s" % ord('a')
print "===================================="
print "pow()"
print "Return x to the power y;"
print "pow(2,5) is %s" % pow(2,5)
print "===================================="
print "print()"
print "===================================="
print "property()"
print "Return a property attribute for new-style classes (classes that derive from object)."
print "Mostly used as a decorator to give a nice name to a function that can be called as an attribute"
print "===================================="
print "range()"
print " create lists containing arithmetic progressions., start, stop ,step as args"
print "range(5,11,2) gives %s" % range(5,11,2)
print "===================================="
print "raw_input()"
print "===================================="
print "===================================="
print "reduce()"
print "Apply function of two arguments cumulatively to the items of iterable (func, iterable, initializer)"
print "reduce(lambda x,y:x+y,range(101)) gives %s" % reduce(lambda x,y:x+y,range(101))
print "===================================="
print "reload()"
print "Reload a previously imported module. Not really used in Dev that often"
print "===================================="
print "repr()"
print "Return a string containing a printable representation of an object. "
print "repr('test') returns %s" % repr('test')
print "===================================="
print "reversed()"
print "===================================="
print "round()"
print "===================================="
print "set()"
print "===================================="
print "setattr()"
print "===================================="
print "slice()"
print "returns a slice object, used by library writers so y=slice(1,11,3) has a start,stop and step indexes, y.step = %s" % slice(1,11,3).step
print "===================================="
print "sorted()"
print "a NEW, sorted copy of an iterable"
print "sorted([5,3,2,6,5]) gives %s" % sorted([5,3,2,6,5])
print "===================================="
print "staticmethod()"
print "Return a static method for function. Used in classes -- gets rid of the 'self'"
print "===================================="
print "str()"
print "Return a string containing a nicely printable representation of an object."
print "str('test') is %s" % str('test')
print "===================================="
print "sum()"
print "Sums start and the items of an iterable from left to right and returns the total."
print "sum(range(101)) gives %s" % sum(range(101))
print "===================================="
print "super()"
print "===================================="
print "tuple()"
print "Return a tuple whose items are the same and in the same order as iterable' items."
print "tuple([1,2,3,4,5]) returns %s and has type of %s" % (tuple([1,2,3,4,5]), type(tuple([1,2,3,4,5])))
print "===================================="
print "type()"
print "2 uses -- called as type(object) gives the type"
print "called with type(name, bases, dict) -- creates a new class"
print "type(1) gives %s" % type(1)
print "type('yy', str, dict(a=1)) gives %s" % type('yy', (object,), dict(a=1))
print "===================================="
print "unichr()"
print "Return the Unicode string of one character whose Unicode code is the integer i."
print "unichr(97) gives %s" % unichr(97)
print "===================================="
print "unicode()"
print "Return the Unicode string version of object"
print "unicode('ggg') gives %s" % unicode('ggg')
print "===================================="
print "vars()"
print "Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute."
tst= type('yy', (object,), dict(a=1))
print "vars(tst) (where tst is type('yy', (object,), dict(a=1))) gives %s" % vars(tst)
print "===================================="
print "xrange()"
print "memory friendly range()"
print "xrange(5,11,2) gives %s" % xrange(5,11,2)
print "===================================="
print "zip()"
print "This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables."
print "zip([1,2,3], [4,5,6]) gives %s" % zip([1,2,3], [4,5,6])
print "===================================="
print "__import__()"
print "This function is invoked by the import statement."
print "this is a dynamic way to import code only at runtime -- advanced jutsu"
print "===================================="
print "apply()"
print "deprecated -- don't use this"
print "===================================="
print "buffer()"
print "deprecated -- don't use this"
print "===================================="
print "coerce()"
print "deprecated -- don't use this"
print "===================================="
print "intern()"
print "deprecated -- don't use this"
print "===================================="