import re

cache = {}
matcher = re.compile("([2-9]99[2-9])|([3-9]88[3-9])|([4-9]77[4-9])")
ending_zeros = re.compile("(.+)(0+$)")


def do_it(int_in):
    # if int_in == 9000:
    #     print("bummer")
    work_unit = str(int_in)
    st = 0
    end = len(work_unit)
    truth_list = [0 for _x in range(end)]
    tmp = 0

    # Filter on bad patterns
    xx = matcher.search(work_unit)
    if xx:
        return truth_list

    # Try and use a cache and regular expressions
    pp = ending_zeros.search(work_unit)
    if pp:
        if cache.get(pp.group(1)) == 1:
            return [1 for _x in range(end)]

    # end filter
    while st < end:
        sub_while = st
        while tmp < 10:
            variable_under_the_scope = int(work_unit[sub_while])
            tmp = tmp + variable_under_the_scope
            sub_while += 1
            if sub_while >= end:
                break

        if tmp == 10:
            for p in range(st, sub_while):
                truth_list[p] = 1
        tmp = 0

        st += 1

    # trailing zero hack
    for x, val in enumerate(work_unit):
        if int(val) == 0:
            if truth_list[int(x) - 1] == 1:
                truth_list[int(x)] = 1
    return truth_list


if __name__ == '__main__':

    import datetime

    start_time = datetime.datetime.now()
    print(start_time)
    cnt = 0
    power_of_ten = 7
    for x1 in range(pow(10, power_of_ten) + 1):
        tst = do_it(x1)
        if x1 % 1000000 == 0:
            print("len is", x1, datetime.datetime.now())
        if all(tst):
            cnt += 1
            cache[str(x1)] = 1
            # print(x1)
    print(cnt)
    end_time = datetime.datetime.now()
    print(end_time - start_time)
