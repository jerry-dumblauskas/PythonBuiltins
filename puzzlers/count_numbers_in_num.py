__author__ = 'jerrydumblauskas'

"""
from 'cracking the coding interview' 5th edition

problem 18.4 write a method to count the number of 2's
between 0 and n (inclusive)
"""


def count_twos(inclusive_num):
    """
    implementation of 18.4
    :param inclusive_num: integer
    :return: count of 2's ('tis an int)
    """
    cnt = 0
    for l_num in range(inclusive_num + 1):
        for item in list(str(l_num)):
            if item == '2':
                cnt+=1

    return cnt

if __name__ == "__main__":
    import timeit
    assert 10 == count_twos(26)
    print (timeit.timeit('count_twos(22)', number=10000, globals=globals()))


