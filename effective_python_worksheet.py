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

# Item 16 ...
print("====ITEM 16: Consider Generators Instead of Returning Lists ====")

print("for large datasets -- generators are the way to go")
print("also reduces visual noise")


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result
address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
result = list(index_words_iter(address))
print(result[:3])


# Item 17 ...
print("====ITEM 17: Be Defensive When Iterating Over Arguments ====")

print("You can easily define your own iterable container type by implementing the __iter__ method as a generator.")
print("the big picture here is that an iterator can be exhausted in a method, it can be used only once")


def issue(m_iter):
    """
    iterable will work, iterator, not so much
    :param m_iter: iterable
    :return: indeed, what will we return?
    """
    print (sum(m_iter))
    rtn = []
    for x in m_iter:
        rtn.append(x)
    return rtn


def m_iterator():
    for i in range(6):
        yield i

print ("This won't work")
lst=[0,1,2,3,4,5]
print (issue(lst))
print (issue(m_iterator()))


class wrap_generator_in_an_iterable(object):
    """
    wrapping class container that creates a new generator on each call
    :return: new container class
    """
    def __init__(self):
        pass

    def __iter__(self):
        return m_iterator()


print ("This will work says Bruce")
print (issue(lst))
print (issue(wrap_generator_in_an_iterable()))


# Item 18 ...
print("====ITEM  18: Reduce Visual Noise with Variable Positional Arguments ====")

print("this is just using *args, i.e wrap in a tuple from basics.py")


def wrap_in_a_tuple(*args):
    for x in args:
        print (x)

a=1
b=2
c=3
d=4

wrap_in_a_tuple(a,b,c)
wrap_in_a_tuple(a,b,c,d)

# Item 19 ...
print("====ITEM 19: Provide Optional Behavior with Keyword Arguments ====")

print("advantages: The first advantage is that keyword arguments make the function call clearer to new readers of the code")
print("also provides a default (just watch for the mutable trap")

def foo(x=1,y=3):
    return x+y

print (foo())
print (foo(1,3))
print (foo(x=4,y=0))
print (foo(y=6, x= -2))


# Item 20 ...
print("====ITEM 20: Use None and Docstrings to Specify Dynamic Default Arguments ====")

print("remember -- this is the default list idiom == the default arg value is evauated at module def time")
print("so, for a list, that is one object, and if you call it 20 times with the default, it will us the same object")
print("also, document this in a doc string")


def my_bad(x=2, lst=[]):
    lst.append(x)
    return lst

print (my_bad(1))
print (my_bad(2))
print ("1 shouldn't be there!")


def my_good(x=2, lst=None):
    """
    A better example
    :param x: item to be listed
    :param lst: the list to add to, if None create a new list
    :return: the listed variable
    """
    lst = lst or []
    lst.append(x)
    return lst

print (my_good(1))
print (my_good(2))
print ("1 isn't there!")


# Item 21 ...
print("====ITEM 21: Enforce Clarity with Keyword-Only Arguments ====")

print("in python3, you can force args to be called with a keyword")
print("below, the safe div function uses a * to say 'after this only keywords, ie, can't cheat and use positional")
def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):

    try:
            return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

try:
    safe_division_c(1, 10**500, True, False)
except Exception as e:
    print (e)

print (safe_division_c(1, 0, ignore_zero_division=True))
print (safe_division_c(1, 1))
print (safe_division_c(1, 2, ignore_zero_division=True))


# Item 22 ...
print("====ITEM 22: Prefer Helper Classes Over Bookkeeping with Dictionaries and Tuples ====")

print("if you need too many lists and dicts in a single class, refactor the complexity out with helper classes")
print("...")


class WeightedGradebook(object):
    # ...
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
           subject_avg, total_weight = 0, 0
           for score, weight in scores:
               pass
        return score_sum / score_count

print (" vs .. ")

import collections
Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

# Item 23 ...
print("====ITEM 23: Accept Functions for Simple Interfaces Instead of Classes ====")

print("use small functions instead of classes when passing in parameters")
names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)
print ("no need for a class in the above")

# Item 24 ...
print("====ITEM Use @classmethod Polymorphism to Construct Objects Generically ====")

print("This is hard to demo -- but ")
print("...")

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
print("====ITEM  ====")

print("...")
print("...")



