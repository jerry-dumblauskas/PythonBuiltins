def do_it(in_num):
    acc = 0
    hot_items = {}

    for x in range(pow(10, in_num) + 1):
        # if x != 3523014:
        #     continue
        # if x == 190:
        #     print("break")
        lst = []
        sub_x = x
        if x > 10:
            short_circuit = hot_items.get(int(str(x)[:-1]), 0)
            if short_circuit != 0:
                last = short_circuit
                real_last = int(str(x)[-1])
                if (last + real_last == 10) or real_last == 0:
                    acc += 1
                    print(x)
                    hot_items[x] = int(str(x)[-1])
                    continue

        for y in str(sub_x):
            lst.append(int(y))
        if x % 1000000 == 0:
            import datetime
            print("len is", x, datetime.datetime.now())

        pos_lst = [0 for _x in range(len(lst))]

        for pos, y in enumerate(lst):
            lst_seg = do_algo(pos, lst)
            for p in lst_seg:
                pos_lst[p] = 1
        if all(pos_lst):
            acc += 1
            print(x)
            hot_items[x] = int(str(x)[-1])
    return acc


def do_algo(x, in_lst):
    tmp_l = 0
    left_x = x
    right_x = x
    lst = []
    while left_x >= 0:
        tmp_l = tmp_l + in_lst[left_x]
        if tmp_l == 10:
            return lst
        if tmp_l > 10:
            break
        lst.append(left_x)
        left_x -= 1
    lst = []
    tmp_r = 0
    while right_x < len(in_lst):
        tmp_r = tmp_r + in_lst[right_x]
        if tmp_r == 10:
            return lst
        if tmp_r > 10:
            break
        lst.append(right_x)
        right_x += 1
    return []


def do_it2(int_in):
    work_unit = str(int_in)
    st = 0
    end = len(work_unit)
    truth_list = [0 for _x in range(end)]
    tmp = 0
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
    # print(do_it2(3523014))
    # print(do_it2(28546))
    import datetime
    start_time = datetime.datetime.now()
    print(start_time)
    cnt = 0
    for x1 in range(pow(10, 7) + 1):
        tst = do_it2(x1)
        if x1 % 1000000 == 0:

            print("len is", x1, )
        if all(tst):
            cnt += 1
            # print(x)
    print(cnt)
    end_time = datetime.datetime.now()
    print(end_time)
    print(end_time - start_time)

    # print(do_it2(190))
    # assert 3492 == do_it(5)
