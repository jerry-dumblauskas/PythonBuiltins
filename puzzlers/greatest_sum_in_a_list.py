import sys


__author__ = 'jerrydumblauskas'

"""
from 'cracking the coding interview' 5th edition

problem 17.8 write a method find the greatest congruent sequence of numbers in a list
(this means sum up the list from start to end)
i.e [2,-8,3,-2,4,-10] gives 5

"""


def find_max(in_lst):
    """
    17.8 in cracking the coding interview

    :param in_lst:
    :return: the sum (an int)
    """

    high_val = sum(in_lst) - 1
    for st_point in range(len(in_lst)):
        for end_point in reversed(range(len(in_lst))):
            slc = in_lst[st_point:end_point + 1]
            if sum(slc) > high_val:
                high_val = sum(slc)

    return high_val
