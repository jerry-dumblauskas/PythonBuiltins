"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
"""

the_number = 1
cont = True
while cont:
    we_passed = True
    for i in range(1, 21):
        if the_number % i != 0:
            we_passed = False
            break
    if we_passed:
        break

    the_number += 1
print(the_number)
