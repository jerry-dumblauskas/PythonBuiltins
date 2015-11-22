__author__ = 'jerrydumblauskas'

import sys
# Item 1 version
print("====ITEM 1 -- Know which version you are using ====")

print((sys.version_info))
print((sys.version))

# Item 2 Pep 8
print("====ITEM 2 -- Use PEP 8!! ====")

print("pip install pylint, and use it!")

# Item 3 Know the Differences Between bytes, str, and unicode
print("====ITEM 3 -- Know the Differences Between bytes, str, and unicode ====")

print("for py2 just str and unicode")
print("str is raw 8 bit values -- unicode is all else")
print("str is the lowest level -- the thing you encode to (the binary representation)")
print("string to unicode ----- you must decode the string")
print("unicode to string ----- you must encode the unicode")

# Item 4 Write Helper Functions Instead of Complex Expressions
print("====ITEM 4 -- Write Helper Functions Instead of Complex Expressions ====")

print("this is a stylistic rule -- what some consider clear and concise")
print("some will consider obtuse and bloated")
print("the rule here is don't show off your one line ability")

# Item 5 Know How to Slice Sequences
print("====ITEM 5 -- Know How to Slice Sequences ====")

print("using this list a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']")
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("a[0;5] == a[:5] so do that")
print(a[:5])
print(a[:-1])
print("remember -- slices make copies of the list!")
print(id(a))
r=a[-5:]
r[0] = 5
print(r)
print(id(r))
print(a)

# Item 6 ...
print("====ITEM 6 -- Avoid Using start, end, and stride in a Single Slice====")
print(a[::-2])

print("hard to read a[0:6:-3], and what does it return (it's a trick)")
print("in this case starts at 0, and goes back, and since there is nothing......")
print("so [::-1] works because == If i or j are omitted or None, they become 'end' values (which end depends on the SIGN of k)")
print(a[0:6:-3])


# Item 7 ...
print("====ITEM 7 Use List Comprehensions Instead of map and filter ====")

b = [1,2,3,4,5,6,7,8,9]
print("map and filters need lambdas (or at least a function")
print("squares = [x**2 for x in b] ")
print([x**2 for x in b])
print("vs")
print("squares = map(lambda x: x ** 2, b)")
print([x ** 2 for x in b])


# Item 8 ...
print("====ITEM 8 Avoid More Than Two Expressions in List Comprehensions ====")

print("This is a simple one, no code needed, as I don't want to write a convoluted example to say")
print("DON'T DO THAT")


# Item 9 ...
print("====ITEM 9 Consider Generator Expressions for Large Comprehensions ====")

print("if large, you can run out of memory")
print("value = [len(x) for x in open('/tmp/my_file.txt')]")
print("what if my_file is 10 gig??")
print("try it = (len(x) for x in open('/tmp/my_file.txt'))")
print("call by it.next()")
print("also, Generator expressions can be composed by passing the iterator from one generator expression into the for subexpression of another.")
print(" i.e -- you can chain them")

# Item 10 ...
print("====ITEM Item 10: Prefer enumerate Over range ====")

print("like range, but gives you a tuple with position")
print("range(10) vs enumerate(10) vs enumerate(10,1)")
print(list(range(10)))
print(list(enumerate(range(10))))
print(list(enumerate(list(range(10)),1)))


# Item 11 ...
print("====ITEM 11: Use zip to Process Iterators in Parallel ====")

print("two or more iterators can be processed in parallel")
print("in python output is full, in 3 gives an iterator")
print(list(zip(enumerate(range(10)), enumerate(list(range(10)), 1))))

# Item 12 ...
print("====ITEM 12 Avoid else Blocks After for and while Loops ====")

print("this is stylistic, but valid -- not many people know this")
print("this else should be called 'nobreak' ")

# Item 13 ...
print("====ITEM 13: Take Advantage of Each Block in try/except/else/finally ====")

print("stylistic")
print("try:")
print(" something")
print("except Exception as e:")
print(" handle exception")
print("else:")
print(" no exception, was ok")
print("finally:")
print(" no matter what run this")

print("not sure I agree with the else clause here")

# Item 14 ...
print("====ITEM 14: Prefer Exceptions to Returning None====")

print("This means 'don't bury exceptions -- let the caller deal with it")


def foo(a,b):
    try:
        rtn = a/b
    except ZeroDivisionError as e:
        print(">" + str(e) + "< This is the exception you should reraise, i.e 'raise e'")
    else:
        return rtn

foo(4,0)

# Item 15 ...
print("====ITEM 15: Know How Closures Interact with Variable Scope ====")

print("in below functions 'helper' can see group")

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

print("helper function using py3 idiom nonlocal, so we can assign inside a function")
def sort_priority2(values, group):
    found = False
    def helper1(x):
        nonlocal found
        if x in group:
            found = True
            return (0,x)
        return (1,x)
    values.sort(key=helper1)
    return found

found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)
# Item 25 ...
print("====ITEM  25: Initialize Parent Classes with super ====")

print("use super -- it defines a mro and ensures things run only once")
print("note -- the __class__ idiom for python 3 is not working as described in the book -- gotta check that out")


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class Explicit(MyBaseClass):
    def __init__(self, value):
        super(Explicit, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)

assert Explicit(10).value == Implicit(10).value

# Item __ ...
print("====ITEM _ -- ====")

print("...")
print("...")

