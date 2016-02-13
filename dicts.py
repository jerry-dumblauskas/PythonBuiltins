from collections import defaultdict, OrderedDict, namedtuple

__author__ = 'jerrydumblauskas'

"""
recipe 1 -- you have a dict, you want to extract a sub dict
based on a list of keys
"""
print("=====Recipe 1 -- dicts")
main_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5, 'g': 6, 'h': 7}
sub_lst = ['a', 'h', 'g']
sub_dict = dict([x for x in main_dict.items() if x[0] in sub_lst])

print("the dict is:" + str(main_dict))
print("here is the list of keys:" + str(sub_lst))
print("after the one line method:" + str(sub_dict))

"""
recipe 2 (and one of the most important items)
when you iterate over a dict you iterate over keys!
"""
print("=====Recipe 2 -- if you iterate over a dict you iterate over the keys")
if 'f' in main_dict:
    print("true -- f the key was in the dict")

if 'z' in main_dict:
    print("true")
else:
    print("false -- z the key was not in the dict")

"""
recipe 3 -- sets are important also!
"""
print("=====Recipe 3 -- sets")
lst = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
m_set = set(lst)
print(lst, " the list")
print(m_set, " after set is called")
another_set = {4, 5, 6, 7}

print(m_set.intersection(another_set), " set intersection")
print(m_set & another_set)
print(m_set.union(another_set))
print(m_set | another_set)

print("set literals -- they look like dict but are sets")
print("so, {{1,2,2,2,3}} will create a set of {}".format({1, 2, 2, 2, 3}))

"""
recipe 4 -- OrderedDict
"""
print("=====Recipe 4 -- OrderedDict")

tst1 = OrderedDict((('z', 1), ('a', 3), ('c', 4), ('k', 7)))
tst2 = OrderedDict([('s', 1), ('t', 3), ('a', 4), ('n', 7)])
print(tst1)

for k, v in tst1.items():
    print(str(k) + ":" + str(v))

rtx = zip(tst1, tst2)
for x in rtx:
    print(x)

"""
recipe 5 -- DefaultDict
"""
print("=====Recipe 5 -- defaultdict")

tst_dict = defaultdict(int)
print("no key gives back", tst_dict['no_key'])

"""
recipe 6 -- namedtuple
"""
print("=====Recipe 6 -- namedtuple")

my_tup = namedtuple('my_tup', "a b c d")

tst = my_tup([], 2, 3, "mix up")

print("access a tuple by name:", tst.d, ":", tst.a, ":", tst.b)

"""
recipe 7 -- dict.items
in py3 items returns a 'dictionary view', which is
a class that you can get an iter from
note that views are now created fro .key() an .values() as well
"""
print("=====Recipe 7 -- dict.items")
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
dishes_items = dishes.items()
print('can get the len by calling len(dictview) on the view')
# noinspection PyTypeChecker
print('so len(dishes_items) is:', len(dishes_items))
print("can get an iterator with iter(view")
print("so, this gives", type(iter(dishes_items)))
print("finally, you do an in check")
print("in this case, for items(), use a tuple")
print("so ('spam',500) in dishes is:", ('spam', 500) in dishes_items)

"""
recipe 8 reverse a dictionary
"""
print("=====Recipe 8 -- reverse a dictionary")
tst_dict = {'a': 1, 'b': 2, 'c': 3}
print("start dict is:", tst_dict)
print("reversed dict is:", dict([(x, y) for (y, x) in tst_dict.items()]))

"""
recipe 9 splat a dict
"""
print("=====recipe 9 splat a dict")
tst_dict = {'a': 'alpha', 'b': 2, 'c': 'charlie'}


def foo(a, b, c):
    print("this is {0}, and this is {2}, and this is {1}".format(a, b, c))


foo(**tst_dict)
