__author__ = 'jerrydumblauskas'

"""
recipe 1 -- you have a dict, you want to extract a sub dict
based on a list of keys
"""
print("=====Recipe 1 -- dicts")
main_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'f':5, 'g':6, 'h':7}
sub_lst = ['a', 'h', 'g']
sub_dict = dict([x for x in main_dict.items() if x[0] in sub_lst])

print ("the dict is:" + str(main_dict))
print ("here is the list of keys:" + str(sub_lst))
print ("after the one line method:" + str(sub_dict))

"""
recipe 2 (and one of the most important items)
when you iterate over a dict you iterate over keys!
"""
print("=====Recipe 2 -- if you iterate over a dict you iterate over the keys")
if 'f' in main_dict:
    print ("true -- f the key was in the dict")

if 'z' in main_dict:
    print(("true"))
else:
    print (("false -- z the key was not in the dict"))

"""
recipe 3 -- sets are important also!
"""
print("=====Recipe 3 -- sets")
lst=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
m_set = set(lst)
print (lst, " the list")
print (m_set, " after set is called")
another_set={4,5,6,7}

print (m_set.intersection(another_set), " set intersection")
print (m_set & another_set)
print (m_set.union(another_set))
print (m_set | another_set)

"""
recipe 4 -- OrderedDict
"""
print("=====Recipe 4 -- OrderedDict")
from collections import OrderedDict
tst1 = OrderedDict((('z',1), ('a',3), ('c',4), ('k',7)))
tst2 = OrderedDict([('s',1), ('t',3), ('a',4), ('n',7)])
print (tst1)

for k, v in tst1.items():
    print (str(k) + ":" + str(v))

rtx = zip(tst1, tst2)
for x in rtx:
    print (x)

"""
recipe 5 -- DefaultDict
"""
print("=====Recipe 5 -- defaultdict")
from collections import defaultdict

tst_dict = defaultdict(int)
print("no key gives back", tst_dict['nokey'])