
def check_it(in_lst):
    """
    this function accepts a sorted list, then looks for the ONE missing number in the list
    the missing number can't be at the start or the end of the list
    :param in_lst:
    :return: the missing number
    """

    st_val = in_lst[0]
    half_pt = len(in_lst)/2
    half_val = in_lst[int(half_pt)]

    # final exit point -- when 2 items are left in the list
    if len(in_lst) <= 2:
        return in_lst[0] + 1

    # Slicing logic, keep cutting down till 2 points are left
    if half_val == half_pt + st_val:
        rtn = check_it(in_lst[int(half_pt):])
    else:
        rtn = check_it(in_lst[:int(half_pt) + 1])
    return rtn


if __name__ == "__main__":

    x = [0,2,3,4,5,6,7,8, 9,10]
    assert  check_it(x) == 1
    print(check_it(x))
    x = list(range(100))
    x.remove(0)
    print(x)
    print(check_it(x))
