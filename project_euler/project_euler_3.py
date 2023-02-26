"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(in_num):
    if in_num <= 0:
        raise Exception(" invalid number, make it > 0")
    if in_num < 3:
        return True
    if in_num % 2 == 0:
        return False

    for chk in range(3, int(in_num / 2), 2):
        if in_num % chk == 0:
            return False
    return True


if __name__ == '__main__':
    my_num = 600851475143
    largest = 0
    divisor = 2
    while True:
        tst_num = my_num / divisor
        if tst_num == int(my_num / divisor):
            if is_prime(tst_num):
                largest = tst_num
                break
        divisor += 1

    print(largest)
