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
    max_val = 0
    for row in range(17):
        for col in range(17):
            num1 = int(dta[row][col])
            num2 = int(dta[row + 1][col + 1])
            num3 = int(dta[row + 2][col + 2])
            num4 = int(dta[row + 3][col + 3])
            l_val = num1 * num2 * num3 * num4
            if l_val > max_val:
                max_val = l_val

    for row in range(19, 0, -1):
        for col in range(17):
            num1 = int(dta[row][col])
            num2 = int(dta[row - 1][col + 1])
            num3 = int(dta[row - 2][col + 2])
            num4 = int(dta[row - 3][col + 3])
            l_val = num1 * num2 * num3 * num4
            if l_val > max_val:
                max_val = l_val
    return max_val


# main
if __name__ == '__main__':
    row_lst = get_data()
    hor = horizontal_max(row_lst)
    vert = vertical_max(row_lst)
    diagonal = diagonal_max(row_lst)
    print(f'vert={vert}, hor={hor}, diagonal={diagonal}')
    print(max(hor, vert, diagonal))
