def do_it(in_num):
    acc = 0
    hot_items = {}

    for x in range(pow(10, in_num) + 1):
        # if x != 3523014:
        #     continue
        # if x != 5:
        #     continue
        lst = []
        if x > 10:
            short_circuit = hot_items.get(int(str(x)[:-1]), 0)
            if short_circuit != 0:
                last = short_circuit
                real_last = int(str(x)[-1])
                if last + real_last == 10:
                    acc += 1
                    hot_items[x] = int(str(x)[-1])
                    continue
        for y in str(x):
            lst.append(int(y))
        if x % 1000000 == 0:
            print("len is", x)

        pos_lst = [0 for _x in range(len(lst))]

        for pos, y in enumerate(lst):
            lst_seg = do_algo(pos, lst)
            for p in lst_seg:
                pos_lst[p] = 1
        if all(pos_lst):
            acc += 1
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


if __name__ == '__main__':
    print(do_it(18))
