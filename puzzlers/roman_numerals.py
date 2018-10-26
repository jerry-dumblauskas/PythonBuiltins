value_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def calc_number(roman_string):
    rtn = 0
    previous_item = None
    for item in roman_string:
        if previous_item:
            if value_dict.get(previous_item) < value_dict.get(item):
                rtn = rtn - value_dict.get(previous_item)
                rtn = rtn + value_dict.get(item) - value_dict.get(previous_item)
                continue
        rtn = rtn + value_dict.get(item)
        previous_item = item
    return rtn


if __name__ == '__main__':
    print(calc_number("MMIV"))
