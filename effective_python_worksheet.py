__author__ = 'jerrydumblauskas'

import sys
# Item 1 version
print "====ITEM 1 -- Know which version you are using ===="

print(sys.version_info)
print(sys.version)

# Item 2 Pep 8
print "====ITEM 2 -- Use PEP 8!! ===="

print "pip install pylint, and use it!"

# Item 3 Know the Differences Between bytes, str, and unicode
print "====ITEM 3 -- Know the Differences Between bytes, str, and unicode ===="

print "for py2 just str and unicode"
print "str is raw 8 bit values -- unicode is all else"
print "str is the lowest level -- the thing you encode to (the binary representation)"
print "string to unicode ----- you must decode the string"
print "unicode to string ----- you must encode the unicode"

# Item 4 Write Helper Functions Instead of Complex Expressions
print "====ITEM 4 -- Write Helper Functions Instead of Complex Expressions ===="

print "this is a stylistic rule -- what some consider clear and concise"
print "some will consider obtuse and bloated"
print "the rule here is don't show off your one line ability"

# Item 5 Know How to Slice Sequences
print "====ITEM 5 -- Know How to Slice Sequences ===="

print "using this list a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']"
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print "a[0;5] == a[:5] so do that"
print a[:5]
print a[:-1]
print "remember -- slices make copies of the list!"
print id(a)
r=a[-5:]
r[0] = 5
print r
print id(r)
print a


# Item 6 ...
print "====ITEM 6 -- Avoid Using start, end, and stride in a Single Slice===="

print "..."
print "..."


# Item 7 ...
print "====ITEM 7 -- ===="

print "..."
print "..."


# Item _ ...
print "====ITEM _ -- ===="

print "..."
print "..."

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print flat

matrix1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flat1 = [x[0] for x in matrix1]
print flat1

def pop(x):
    print x


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)


def sort_priority2(values, group):
    found = [False]
    def helper1(x):
        if x in group:
            found[0] = True
            return (0,x)
        return (1,x)
    values.sort(key=helper1)
    return found[0]
