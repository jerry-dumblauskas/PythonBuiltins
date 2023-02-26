import math

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def find_primes(in_max):
    num_sqrt = int(math.sqrt(in_max))
    raw_primes_lst = list(range(in_max + 1))
    iterating_lst = list(range(in_max + 1))
    for i in range(len(iterating_lst)):
        if i in (0, 1):
            raw_primes_lst[i] = 0
            continue
        run_var = int(math.pow(i, 2))
        while True:
            if run_var > in_max:
                break
            raw_primes_lst[run_var] = 0
            run_var += i

        if iterating_lst[i] == num_sqrt:
            break

    final_primes_lst = []
    for y in raw_primes_lst:
        if y > 0:
            final_primes_lst.append(y)
    return final_primes_lst


if __name__ == '__main__':
    x = find_primes(2000000)
    print(sum(x))
