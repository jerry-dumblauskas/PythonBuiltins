"""
interview question -- implement power, without a for loop, and without using pow
"""
from functools import reduce
from operator import mul

def answer1(bse, pwr):
    if pwr == 0:
        return 1
    return answer1(bse, pwr-1) * bse

def answer2(bse, pwr):
    return reduce(mul, [bse] * pwr)

if __name__ == "__main__":
    tst_answer = answer1(2, 5)
    if 32 != tst_answer:
        print(tst_answer)
        raise Exception("failed! answer does not match")
    tst_answer = answer2(2, 5)
    if 32 != tst_answer:
        print(tst_answer)
        raise Exception("failed! answer does not match")