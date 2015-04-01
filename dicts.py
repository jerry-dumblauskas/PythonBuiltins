__author__ = 'jerrydumblauskas'

'''
idiom -- you have a dict, you want to extract a sub dict
based on a list of keys
'''
main_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'f':5, 'g':6, 'h':7}
sub_lst = ['a', 'h', 'g']
sub_dict = dict([x for x in main_dict.items() if x[0] in sub_lst])

print main_dict
print sub_dict

