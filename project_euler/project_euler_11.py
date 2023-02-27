import math


def get_data():
    dta = open("./f_11.txt", 'r')
    lst_of_lists = []
    for line in dta:
        row = line.strip().split(" ")
        lst_of_lists.append(row)
    print(lst_of_lists)
    return lst_of_lists


def horizontal_max(dta):
    max_val = 0
    for row in dta:
        # 0 1 2 3 4 5
        row = [int(i) for i in row]
        for cnt, item in enumerate(row):
            if len(row) - cnt < 4:
                break
            tst = math.prod(row[cnt:4 + cnt])
            if tst > max_val:
                max_val = tst

    return max_val


def vertical_max(dta):
    transposed_lst = []
    for i in range(len(dta[0])):
        tmp_lst = []
        for lst in dta:
            tmp_lst.append(lst[i])
        transposed_lst.append(tmp_lst)
    print(transposed_lst)
    return horizontal_max(transposed_lst)


def diagonal_max(dta):
    return len(dta)


# main
if __name__ == '__main__':
    row_lst = get_data()
    vert = vertical_max(row_lst)
    hor = horizontal_max(row_lst)
    diagonal = diagonal_max(row_lst)
    print(max(hor, vert, diagonal))
