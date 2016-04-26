import collections
import copyreg
import logging
import pickle
import select
import subprocess
import sys
import tempfile
import time as tm
import tracemalloc
from bisect import bisect_left
from cProfile import Profile
from collections import deque, OrderedDict, defaultdict
from collections.abc import Sequence
from concurrent.futures import ProcessPoolExecutor
from contextlib import contextmanager
from datetime import datetime, timezone
from decimal import Decimal, ROUND_UP
from functools import wraps
from heapq import heappush, heappop
from pstats import Stats
from queue import Queue
from random import randint
from threading import Thread, Lock
from time import mktime
from time import time
from weakref import WeakKeyDictionary

import pytz

__author__ = 'jerrydumblauskas'

# Item 1 ...
print("====ITEM 1: Know which version you are using ====")

print(sys.version_info)
print(sys.version)

# Item 2 ...
print("====ITEM 2: Use PEP 8!! ====")

print("pip install pylint, and use it!")
print("use PyCharm's built in tools")

# Item 3 ...
print("====ITEM 3: Know the Differences Between bytes, str, and unicode ====")

print("for py2 just str and unicode")
print("str is raw 8 bit values -- unicode is all else")
print("str is the lowest level -- the thing you encode to (the binary representation)")
print("string to unicode ----- you must decode the string")
print("unicode to string ----- you must encode the unicode")
print("for py3  there are two types that represent sequences of characters: bytes and str.")
print("bytes are raw, str contain unicode")
print("so you encode to bytes")

basic_str = 'basic'
print('a basic string is of type', type(basic_str))
basic_b = basic_str.encode()
print('and in py3 this encodes to ', type(basic_b))

# Item 4 ...
print("====ITEM 4: Write Helper Functions Instead of Complex Expressions ====")

print("this is a stylistic rule -- what some consider clear and concise")
print("some will consider obtuse and bloated")
print("the rule here is don't show off your one line ability")

# Item 5 ...
print("====ITEM 5: Know How to Slice Sequences ====")

print("using this list a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']")
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("a[0;5] == a[:5] so do that")
print(a[:5])
print('cut of the last item (a common idiom)', a[:-1])
print("remember -- slices make copies of the list!")
print(str(id(a)) + " the id of the list a")
qq = a[:]
print(str(id(qq)) + " the id of the list qq, which was sliced from a")

print("note that the slice {-x:] will start from x back and go to the end of the list")
r = a[-5:]
print(r)

# Item 6 ...
print("====ITEM 6: Avoid Using start, end, and stride in a Single Slice====")
print(a[::-2])

print("hard to read a[0:6:-3], and what does it return (it's a trick)")
print("in this case starts at 0, and goes back, and since there is nothing......")
print(
    "so [::-1] works because == If i or j are omitted or None, they become 'end' values "
    "(which end depends on the SIGN of k)")
print(a[0:6:-3])

# Item 7 ...
print("====ITEM 7: Use List Comprehensions Instead of map and filter ====")

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("map and filters need lambdas (or at least a function")
print("squares = [x**2 for x in b] ")
print([x ** 2 for x in b])
print("vs")
print("squares = map(lambda x: x ** 2, b)")
print([x ** 2 for x in b])

# Item 8 ...
print("====ITEM 8: Avoid More Than Two Expressions in List Comprehensions ====")

print("DON'T DO THIS")
print("matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
print("filtered = [[x for x in row if x % 3 == 0]")
print("            for row in matrix if sum(row) >= 10]")
print("print(filtered)")

# Item 9 ...
print("====ITEM 9: Consider Generator Expressions for Large Comprehensions ====")

print("if large, you can run out of memory")
print("value = [len(x) for x in open('/tmp/my_file.txt')]")
print("what if my_file is 10 gig??")
print("try it = (len(x) for x in open('/tmp/my_file.txt'))")
print("call by it.next()")
print(
    "also, Generator expressions can be composed by passing the iterator from one "
    "generator expression into the for sub expression of another.")
print(" i.e -- you can chain them")

# Item 10 ...
print("====ITEM 10: Prefer enumerate Over range ====")

print("like range, but gives you a tuple with position")
print("range(10) vs enumerate(10) vs enumerate(10,1)")
print("range(10) =", list(range(10)))
print("enumerate(10) =", list(enumerate(range(10))))
print("enumerate(10,1) =", list(enumerate(list(range(10)), 1)))

# Item 11 ...
print("====ITEM 11: Use zip to Process Iterators in Parallel ====")

print("two or more iterators can be processed in parallel")
print("in python output is full, in 3 gives an iterator")
print(list(zip(enumerate(range(10)), enumerate(list(range(10)), 1))))

# Item 12 ...
print("====ITEM 12 Avoid else Blocks After for and while Loops ====")

print("this is stylistic, but valid -- not many people know this")
print("this else should be called 'nobreak' per Raymond H. ")

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


def foo(first, second):
    try:
        rtn = first / second
    except ZeroDivisionError as foo_exception:
        print(">" + str(foo_exception) + "< This is the exception you should re-raise, i.e 'raise e'")
    else:
        return rtn


foo(4, 0)

# Item 15 ...
print("====ITEM 15: Know How Closures Interact with Variable Scope ====")

print("in below functions 'helper' can see group")


def sort_priority(values, passed_group):
    def helper(item):
        if item in passed_group:
            return 0, item
        return 1, item

    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

print("helper function using py3 idiom nonlocal, so we can assign inside a function")


def sort_priority2(values, passed_group):
    in_found = False

    def helper1(item):
        nonlocal in_found
        if item in passed_group:
            in_found = True
            return 0, item
        return 1, item

    values.sort(key=helper1)
    return in_found


found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)

# Item 16 ...
print("====ITEM 16: Consider Generators Instead of Returning Lists ====")

print("for large datasets -- generators are the way to go")
print("also reduces visual noise")


def index_words(text):
    local_result = []
    if text:
        local_result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            local_result.append(index + 1)
    return local_result


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
    print(sum(m_iter), "in issue method")
    rtn = []
    for item in m_iter:
        rtn.append(item)
    return rtn


def m_iterator():
    for item in range(6):
        yield item


print("As stated, the iterable will work")
lst = [0, 1, 2, 3, 4, 5]
print(issue(lst), " should be the list ", lst)
print("But an iterable will not work")
print(issue(m_iterator()), " should be a list like ", lst)


class WrapGeneratorInAnIterable(object):
    """
    wrapping class container that creates a new generator on each call
    :return: new container class
    """

    def __init__(self):
        pass

    def __iter__(self):
        return m_iterator()


print("This will work says Bruce")
print(issue(lst))
print(issue(WrapGeneratorInAnIterable()))

# Item 18 ...
print("====ITEM  18: Reduce Visual Noise with Variable Positional Arguments ====")

print("this is just using *args, i.e wrap in a tuple from basics.py")


def wrap_in_a_tuple(*args):
    for item in args:
        print(item)


a = 1
b = 2
c = 3
d = 4

wrap_in_a_tuple(a, b, c)
wrap_in_a_tuple(a, b, c, d)

# Item 19 ...
print("====ITEM 19: Provide Optional Behavior with Keyword Arguments ====")

print(
    "advantages: The first advantage is that keyword arguments make the function call clearer "
    "to new readers of the code")
print("also provides a default (just watch for the mutable trap")


def foo(bang=1, y=3):
    return bang + y


print(foo())
print(foo(1, 3))
print(foo(bang=4, y=0))
print(foo(y=6, bang=-2))

# Item 20 ...
print("====ITEM 20: Use None and Docstrings to Specify Dynamic Default Arguments ====")

print("remember -- this is the default list idiom == the default arg value is evaluated at module def time")
print("so, for a list, that is one object, and if you call it 20 times with the default, it will us the same object")
print("also, document this in a doc string")


def my_bad(item=2, passed_list=[]):
    passed_list.append(item)
    return passed_list


print(my_bad(1))
print(my_bad(2))
print("1 shouldn't be there!")


def my_good(item=2, passed_list=None):
    """
    A better example
    :param item: item to be listed
    :param passed_list: the list to add to, if None create a new list
    :return: the listed variable
    """
    passed_list = passed_list or []
    passed_list.append(item)
    return passed_list


print(my_good(1))
print(my_good(2))
print("1 isn't there!")

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
    safe_division_c(1, 10 ** 500, True, False)
except Exception as e:
    print(e)

print(safe_division_c(1, 0, ignore_zero_division=True))
print(safe_division_c(1, 1))
print(safe_division_c(1, 2, ignore_zero_division=True))

# Item 22 ...
print("====ITEM 22: Prefer Helper Classes Over Bookkeeping with Dictionaries and Tuples ====")

print("if you need too many lists and dicts in a single class, refactor the complexity out with helper classes")
print("...")


class WeightedGradeBook(object):
    # ...
    def __init__(self):
        self._grades = None

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
                score_sum += score
                total_weight += weight
        return score_sum / score_count


print(" vs .. ")

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


class GradeBook(object):
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
names.sort(key=lambda item: len(item))
print(names)
print("no need for a class in the above")

# Item 24 ...
print("====ITEM Use @classmethod Polymorphism to Construct Objects Generically ====")

print("The below class can be constructed in many ways ")


class MyData:
    def __init__(self, my_data):
        """Initialize MyData from a sequence"""
        self.data = my_data

    @classmethod
    def from_filename(cls, filename):
        """Initialize MyData from a file
        :param filename:
        """
        my_data = open(filename).readlines()
        return cls(my_data)

    @classmethod
    def from_dict(cls, datadict):
        """Initialize MyData from a dict's item
        :param datadict:
        """
        return cls(datadict.items())


myD1 = MyData([1, 2, 3])
print(myD1.data)
myD1 = MyData.from_dict({1: 'one', 2: 'two'})
print(myD1.data)

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

# Item 26 ...
print("====ITEM 26: Use Multiple Inheritance Only for Mix-in Utility Classes ====")

print("mi sucks -- but mix ins are ok")
print("mixin is like adding a static set of functionality into a class")


class BogusMixin(object):
    @staticmethod
    def send_to_space():
        print("blast off")


class MyParent(object):
    def __init__(self):
        pass


class Boring(MyParent, BogusMixin):
    def __init__(self, passed_data):
        super().__init__()
        self.data = passed_data

    def do_work(self):
        self.send_to_space()


b = Boring(77)
print(b.do_work())

# Item 27 ...
print("====ITEM 27: Prefer Public Attributes Over Private Ones ====")

print("a __ in front of a var makes it private")
print("we are all consenting adults -- let's not do this")


class MyClass(object):
    def __init__(self):
        self.__s = 9


try:
    mc = MyClass()
    print(mc.__s)
except Exception as e:
    print("exception is:" + str(e))

print("see!  but you can work around this with a _Class in front")
mc1 = MyClass()
print(mc1._MyClass__s)

# Item 28 ...
print("====ITEM 28: Inherit from collections.abc for Custom Container Types ====")

print('you can just inherit from list....but if you don\'t want to do that')
print('the abc tells you what you need implement, and gives some scaffolding')


class BadType(Sequence):
    def __getitem__(self, item):
        """just need to impl this"""

    def __len__(self):
        """and this..."""


foo = BadType()

# Item 29 ...
print("====ITEM 29: Use Plain Attributes Instead of Get and Set Methods ====")

print("Don't do java -- and if you want some control, use @property to add logic, like so")


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


try:
    r3 = BoundedResistance(1e3)
    r3.ohms = 0
except ValueError as e:
    print(e)

# Item 30 ...
print("====ITEM 30: Consider @property Instead of Refactoring Attributes ====")

print("@property is a tool to help you address problems you’ll come across in real-world code.")
print("Don’t overuse it. When you find yourself repeatedly extending @property methods, it’s ")
print("probably time to refactor your class instead of further paving over your code’s poor design.")
print("...")


class Poop(object):
    def __init__(self, initial_cash=0):
        self.__cash = initial_cash

    def get_cash(self, amount):
        if amount <= self.__cash:
            self.__cash -= amount
            return amount


p = Poop(100)
print(p.get_cash(33))
print(p.get_cash(99))

print("with a @property")


class Poop1(object):
    def __init__(self, initial_cash=0):
        self.__cash = initial_cash

    @property
    def cash(self):
        return self.__cash

    @cash.setter
    def cash(self, amount):
        self.__cash = self.__cash + amount

    def get_cash(self, amount):
        if amount <= self.__cash:
            self.__cash -= amount
            return amount


p = Poop1(100)
print(p.get_cash(33))
p.cash = 55
print(p.get_cash(99))

# Item 31 ...
print("====ITEM 31: Use Descriptors for Reusable @property Methods ====")

print(
    "Define any of these methods and an object is considered a descriptor and can override "
    "default behavior upon being looked up as an attribute.")
print("this example also uses weakref (for memory leaks")
print("descriptors are more generic and reusable then @prop")


class Grades(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


class Exam(object):
    # Class attributes
    math_grade = Grades()
    writing_grade = Grades()
    science_grade = Grades()


exam = Exam()
exam.writing_grade = 99
exam1 = Exam()
exam1.writing_grade = 100

print(exam.writing_grade)
print(exam1.writing_grade)

# Item 32 ...
print("====ITEM Use __getattr__, __getattribute__, and __setattr__ for Lazy Attributes ====")

print(
    "If your class defines __getattr__, that method is called every time an attribute can’t be "
    "found in an object’s instance dictionary.")
print(
    "__getattribute__. This special method is called every time an attribute is accessed on an object,"
    " even in cases where it does exist in the attribute dictionary.")
print(
    "The __setattr__ method is always called every time an attribute is assigned on an instance "
    "(either directly or through the setattr built-in function).")


class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        print("see called only once")
        setattr(self, name, value)
        return value


g = LazyDB()

print("g is:", g.__dict__)
print("g foo is:", g.foo)
print("g foo is(again):", g.foo)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value


data = ValidatingDB()
print('exists:', data.exists)
print('foo:   ', data.foo)
print('foo:   ', data.foo)

print("NOTE -- get_attribute and setattr are called on each access -- you can get caught in a infinite loop")
print("use super to break it")

# Item 33 ...
print("====ITEM 33: Validate Subclasses with Metaclasses ====")

print("Use metaclasses to ensure that subclasses are well formed at the time they are defined, before objects")
print("of their type are constructed.")


class Meta(type):
    def __new__(mcs, name, bases, class_dict):
        print((mcs, name, bases, class_dict))
        if class_dict.get('stuff') != 124:
            print("this could fail if we want")
        return type.__new__(mcs, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 123

    def __init__(self):
        print("in the class init")


pu = MyClass()

# Item 34 ...
print("====ITEM 34: Register Class Existence with Metaclasses ====")

print("Class registration is a helpful pattern for building modular Python programs.")
print("34 is the same as 33, but here you can call a method (instead of, or in addition to, a ")
print("validation check) to register the class for a cache or a lookup")

# Item 35 ...
print("====ITEM 35: Annotate Class Attributes with Metaclasses ====")
print("Metaclasses enable you to modify a class’s attributes before the class is fully defined.")
print("Here, we can cut down on typing")


class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer(object):
    # Class attributes
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')


bar = Customer()
print('Before:', repr(bar.first_name), bar.__dict__)
bar.first_name = 'Euclid'
print('After: ', repr(bar.first_name), bar.__dict__)
print("See how we have to enter in first_name twice???")


class Meta(type):
    def __new__(mcs, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(mcs, name, bases, class_dict)
        return cls


class DatabaseRow(object, metaclass=Meta):
    pass


class Field(object):
    def __init__(self):
        # These will be assigned by the metaclass.
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


bar = BetterCustomer()
print('Before:', repr(bar.first_name), bar.__dict__)
bar.first_name = 'Euler'
print('After: ', repr(bar.first_name), bar.__dict__)
print("only issue is the meta needs to know about the field object -- not sure I like that")

# Item 36 ...
print("====ITEM 36: Use subprocess to Manage Child Processes ====")
print("subprocess is a builtin module")

print("run a simple subprocess -- blocking")

try:
    proc = subprocess.Popen(['echo', 'go home'], stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(out)
    proc = subprocess.Popen(['ps'], stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(proc.pid)

    print("run a simple subprocess -- nonblocking")
    proc = subprocess.Popen(['sleep', '.1'])
    while proc.poll() is None:
        pass
        # print ("lots of work")
    print("exit status...", proc.poll())
except FileNotFoundError as e:
    print("in windows for now....let's fix this later")

print("run a bunch in parallel")


def run_sleep(per):
    local_proc = subprocess.Popen(['sleep', per])
    return local_proc


start = time()
procs = []
try:
    for _ in range(10):
        proc = run_sleep('.1')
        procs.append(proc)

    for proc in procs:
        proc.communicate()
        print(proc.pid)
    end = time()
    print('Finished in %.3f seconds' % (end - start))
except FileNotFoundError as e:
    print("in windows for now....let's fix this later")

# Item 37 ...
print("====ITEM 37: Use Threads for Blocking I/O, Avoid for Parallelism ====")
print("This is the GIL!!  But if you have system io, try threads")


def slow_select():
    try:
        select.select([], [], [], .1)
    except Exception as failed:
        print(failed)


try:
    start = time()
    for _ in range(5):
        slow_select()
    end = time()
    print('Took %.3f seconds' % (end - start))
except OSError as exception:
    print("in windows with an OSError....let's fix this later")
try:
    start = time()
    threads = []
    for _ in range(5):
        thread = Thread(target=slow_select)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end = time()
    print('using IO Took %.3f seconds' % (end - start))
except OSError as e:
    print("in windows for now....let's fix this later")
# Item 38 ...
print("====ITEM 38: Use Lock to Prevent Data Races in Threads ====")
print("even with the gil -- need to lock critical sections")

print("bad way")


class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


def worker(sensor_index, passed_how_many, passed_counter):
    for _ in range(passed_how_many):
        passed_counter.increment(1)


def run_threads(func, passed_how_many, passed_counter):
    local_threads = []
    for items in range(5):
        args = (items, passed_how_many, passed_counter)
        local_thread = Thread(target=func, args=args)
        local_threads.append(local_thread)
        local_thread.start()
    for local_thread in local_threads:
        local_thread.join()


how_many = 10 ** 5
counter = Counter()
run_threads(worker, how_many, counter)
print("Counter should be %d, found %d" % (5 * how_many, counter.count))

print("works")


class LockingCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


counter = LockingCounter()
run_threads(worker, how_many, counter)
print('Counter should be %d, found %d' %
      (5 * how_many, counter.count))

# Item 39 ...
print("====ITEM 39: Use Queue to Coordinate Work Between Threads ====")
print("queue is more efficient that doing it yourself")

q = Queue()


def consumer():
    print("start consumer")
    q.get()
    print("consumer done")


t = Thread(target=consumer)
t.start()

tm.sleep(4)
print("producer putting")
q.put("fff")
thread.join()
print("producer done")

# Item 40 ...
print("====ITEM 40: Consider Coroutines to Run Many Functions Concurrently ====")
print("somewhat related to generators -- the yield can be assigned a value and called by the .send")
print("can chain these together and mimic threads")


def minimize():
    print("start")
    current = yield
    print("end")
    print('current', current)
    while True:
        print("in loop")
        value = yield current
        print('value', value)
        current = min(value, current)


it = minimize()
next(it)
print(it.send(33))
print(it.send(44))

# Item 41 ...
print("====ITEM 41: Consider concurrent.futures for True Parallelism ====")
print("this is the multiprocessing module")


def gcd(pair):
    """
    greatest common divisor
    :param pair: tuple of ints
    :return: int
    """
    first, second = pair
    low = min(first, second)
    for item in range(low, 0, -1):
        if first % item == 0 and second % item == 0:
            return item


numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802)]

start = time()
results = list(map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))

print("using multiprocessing...")

try:
    start = time()
    pool = ProcessPoolExecutor(max_workers=2)  # The one change
    results = list(pool.map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))
except RuntimeError as e:
    print("another windows fail....")

# Item 42 ...
print("====ITEM 42: Define Function Decorators with functools.wraps ====")
print("func tools!!")


def my_dec(func):
    def wrapper():
        print("in wrapper")
        return func()

    return wrapper


@my_dec
def youza():
    print("in youza")


print("calling youza")
youza()
print("here is the issue, the func object has been renamed!!")
print(youza)


def my_dec(func):
    @wraps(func)
    def wrapper():
        print("in wrapper")
        return func()

    return wrapper


@my_dec
def youza():
    print("in youza")


print("calling youza")
youza()
print("here is the FIXED issue, the func object has NOT been renamed!!")
print(youza)

# Item 43 ...
print("====ITEM 43: Consider contextlib and with Statements for Reusable try/finally Behavior ====")
print("no need to handle the __enter__ and __exit__")


def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


print("default is error")
my_function()


@contextmanager
def logging_level(level):
    local_logger = logging.getLogger()
    old_level = local_logger.getEffectiveLevel()
    local_logger.setLevel(level)
    try:
        yield
    finally:
        local_logger.setLevel(old_level)


print('with a context wrapping')
with logging_level(logging.DEBUG):
    print('Inside:')
    my_function()

print("can also set to use with a 'with'")


@contextmanager
def log_level(level, name):
    local_logger = logging.getLogger(name)
    old_level = local_logger.getEffectiveLevel()
    local_logger.setLevel(level)
    try:
        yield local_logger
    finally:
        local_logger.setLevel(old_level)


with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message!')
    logging.debug('This will not print')

# Item 44 ...
print("====ITEM 44: Make pickle Reliable with copyreg ====")
print("Use the copyreg built-in module with pickle to add missing attribute values,")
print("allow versioning of classes, and provide stable import paths.")


class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4


state = GameState()

state_path = tempfile.NamedTemporaryFile().name

with open(state_path, 'wb') as f:
    pickle.dump(state, f)

with open(state_path, 'rb') as f:
    pic = pickle.load(f)
print(pic.__dict__)
print("now to use copyreg")


class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    return GameState(**kwargs)


print("set the pickle constructor to an object type")
copyreg.pickle(GameState, pickle_game_state)
state = GameState()
with open(state_path, 'wb') as f:
    pickle.dump(state, f)

print("change the object type")


class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points
        self.garbage = 999


print("reload from the previous object")
with open(state_path, 'rb') as f:
    pic = pickle.load(f)

print(pic.__dict__)

# Item 45 ...
print("====ITEM 45: Use datetime Instead of time for Local Clocks ====")
print("Avoid using the time module for translating between different time zones.")
print(
    "Use the datetime built-in module along with the pytz module to reliably convert between "
    "times in different time zones.")
print("Always represent time in UTC and do conversions to local time as the final step "
      "before presentation.")

now = datetime(2014, 8, 10, 18, 18, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()

utc_now = mktime(time_tuple)
print(utc_now)

print("and pytz is a db of all time zones")

arrival_nyc = '2014-05-01 23:33:24'
print('arrival_nyc:', arrival_nyc)
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
eastern = pytz.timezone('US/Eastern')
nyc_dt = eastern.localize(nyc_dt_naive)
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
print('utc_dt:', utc_dt)

# Item 46 ...
print("====ITEM  46: Use Built-in Algorithms and Data Structures ====")
print("duh!  DO NOT REINVENT THE FRIGGIN WHEEL!!!")
print("Double Ended Queue")

fifo = deque()
fifo.append(1)
fifo.append(2)
fifo.append(3)
print(fifo.pop())
print(fifo.popleft())

print("Ordered Dict")
a = OrderedDict()
a['foo'] = 1
a['bar'] = 2
b = OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'

for num, col in zip(a.values(), b.values()):
    print(num, col)

print("Default Dict -- suppress key errors")
tst = defaultdict(int)
print("normally this would puck, but now we get the default, which is 0....", tst['no-key'])

print("Heap Queue -- Heaps are useful data structures for maintaining a priority queue. ")
a = []

heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
print(a, " note that 7 is before 5 -- that is because it is first in the tree (visually)")
print(heappop(a), heappop(a), heappop(a), heappop(a))

print("Bisection -- The complexity of a binary search is logarithmic")

x = list(range(10 ** 6))
i = x.index(991234)
print(i)
i = bisect_left(x, 991234)
print(i)

print("IterTools!")
print("The itertools functions fall into three main categories:")
print("Linking iterators together")
print("Filtering items from an iterator")
print(" Combinations of items from iterators")

# Item 47 ...
print("====ITEM 47: Use decimal When Precision Is Paramount ====")
print("IEEE 754 floating point accuracy AND you can control rounding")

rate = 1.45
seconds = 222
cost = rate * seconds / 60
print("==using float")
print(cost)
print(round(cost, 2))
print("==using Decimal")
rate = Decimal('1.45')
seconds = Decimal('222')
cost = rate * seconds / 60
print(cost)
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)

# Item 48 ...
print("====ITEM 48: Know Where to Find Community-Built Modules ====")
print("use Pip or a dist like Conda!")

# Item 49 ...
print("====ITEM 49: Write Docstrings for Every Function, Class, and Module ====")
print("Once you do, the __doc__ can be called -- also, use double quotes")

# Item 50 ...
print("====ITEM 50: Use Packages to Organize Modules and Provide Stable APIs ====")
print("an empty init in a folder makes the folder a package")
print("use the __all__ in the init to expose an 'interface' to callers")

# Item 51 ...
print("====ITEM 51: Define a Root Exception to Insulate Callers from APIs ====")
print("for APIs it’s much more powerful to define your own hierarchy of exceptions.")
print("This way -- a caller to your api can catch just YOUR exception if they want")

# Item 52 ...
print("====ITEM 52: Know How to Break Circular Dependencies ====")
print("Never saw this until BofA, but I guess it happens elsewhere")
print("when a code is loaded, the issue is that in steps 4 and 5")
print("4. Inserts the module into sys.modules")
print("5. Runs the code in the module object to define its contents")
print("after step 4 the circular dep is called, BEFORE the code is run -- and that causes the")
print("issue at step 5 ")
print("best approach is The best way to break a circular dependency is refactoring mutual ")
print("dependencies into a separate module at the bottom of the dependency tree.")
print("don't do dynamic imports i.e import right before the call -- that is hard to read")

# Item 53 ...
print("====ITEM 53: Use Virtual Environments for Isolated and Reproducible Dependencies ====")
print("use pyvenv -- this allows you to test an deploy code -- REMEMBER to source the activate script!!!")
print("pip3 freeze > requirements.txt can be used to create a fi;e you can transfer to a new virtual env")
print("(or to production")
print("in conda use conda create -- same thing")

# Item 54 ...
print("====ITEM 54: Consider Module-Scoped Code to Configure Deployment Environments ====")
print("use a variable to determine things like test and prod db's")
print("use configparser to build config scripts to do the same thing")

# Item 55 ...
print("====ITEM 55: Use repr Strings for Debugging Output ====")
print("Calling print on built-in Python types will produce the human-readable string version of a value,")
print("which hides type information.")
a = '\x07'
print(repr(a))
print(a, " which should be nothing")

# Item 56 ...
print("====ITEM 56: Test Everything with unittest ====")
print("this is so self explanatory :) -- no code needed")
print("oh, but use mock")

# Item 57 ...
print("====ITEM 57: Consider Interactive Debugging with pdb ====")
print("use your ide for the most part :)")

# Item 58 ...
print("====ITEM 58: Profile Before Optimizing ====")
print("use CProfile -- faster than the pure python version")


def insertion_sort(passed_data):
    local_result = []
    for value in passed_data:
        insert_value(local_result, value)
    return local_result


def insert_value(array, value):
    for item, existing in enumerate(array):
        if existing > value:
            array.insert(item, value)
            return
    array.append(value)


max_size = 10 ** 4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

pp = Profile()
pp.runcall(test)

stats = Stats(pp)
stats.strip_dirs()
stats.sort_stats('cumulative')
print("slow======")
stats.print_stats()


def insert_value(array, value):
    item = bisect_left(array, value)
    array.insert(item, value)


test = lambda: insertion_sort(data)
pp = Profile()
pp.runcall(test)
stats = Stats(pp)
stats.strip_dirs()
stats.sort_stats('cumulative')
print("fast==== note the total time compared to the last run")
stats.print_stats()

# Item 59 ...
print("====ITEM 59: Use tracemalloc to Understand Memory Usage and Leaks ====")
print("only in 3.4 and above, figure out what is taking memory")

tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()
l = []
for i in range(1000000):
    l.append('g')

time2 = tracemalloc.take_snapshot()
stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
    print(stat)

stats = time2.compare_to(time1, 'traceback')
top = stats[0]
print("biggest waster")
print('\n'.join(top.traceback.format()))
