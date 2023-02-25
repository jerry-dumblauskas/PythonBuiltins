def answer():
    rtn = 0
    for x in range(1, 1000):
        for y in range(1, 1000):
            tst = y*x
            if is_palindrome(tst):
                if tst > rtn:
                    rtn = tst
    return rtn


def is_palindrome(in_value):
    lst_rev = list(str(in_value))
    lst_rev.reverse()
    return str(in_value) == "".join(lst_rev)


if __name__ == '__main__':
    print(answer())
