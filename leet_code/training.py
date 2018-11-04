def binary_array_to_number(arr):
    rtn = 0
    for i, val in enumerate(reversed(arr)):
        if val:
            rtn = rtn + pow(2, i)
    return rtn

if __name__ == '__main__':
    ar = [0, 1, 1, 0]
    print(binary_array_to_number(ar))
