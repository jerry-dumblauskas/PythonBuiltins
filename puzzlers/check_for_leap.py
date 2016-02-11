"""
check for leap year
the formula is divisible by 4, and if divisible by 100, also must be divisible by 400
use the modulo
"""


def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    if year % 4 == 0:
        return True
    return False
