import math

looper = 1000000


def number_sum(in_number):
    cnt: int
    if in_number % 2 == 0:
        cnt = (1 + in_number) * (in_number / 2)
    else:
        cnt = in_number * ((in_number - 1) / 2) + in_number

    return int(cnt)


def number_of_divisors_lst(in_number):
    cnt = []
    for i in range(1, int((in_number + 1) / 2) + 1):
        if in_number % i == 0:
            cnt.append(i)
    cnt.append(in_number)
    return cnt


def number_of_divisors_fast(in_number):
    cnt = 0
    limit = int(math.sqrt(in_number))
    for item in range(1, limit + 1):
        if in_number % item == 0:
            cnt += 2
    return cnt


"""
It is not the x, but the ns that is the answer
"""
for x in range(12000, looper + 1):
    ns = number_sum(x)
    res1 = number_of_divisors_fast(ns)
    print(f'{x} : {ns} : {res1}')
    if res1 > 500:
        break
