"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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


the_sum = 0
potential_prime = 2000000
while potential_prime > 1:
    if is_prime(potential_prime):
        the_sum += potential_prime
        print(potential_prime)
    potential_prime -= 1

print(the_sum)
