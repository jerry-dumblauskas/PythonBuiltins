def find_substring(search_string, main_string):
    rtn = -1
    good_char_list = get_list_chars_in_search_string(search_string)
    ptr = len(search_string) - 1
    while ptr < len(main_string):
        item = main_string[ptr]
        if item not in good_char_list:
            ptr = ptr + len(search_string)
            continue
        reverse_ptr = ptr
        ss_pointer = len(search_string) - 1
        while ss_pointer >= 0:
            item = main_string[reverse_ptr]
            ss_item = search_string[ss_pointer]
            if item == ss_item:
                reverse_ptr = reverse_ptr - 1
                ss_pointer = ss_pointer - 1
            else:
                ptr = ptr + 1
                break

            if ss_pointer == 0:
                return reverse_ptr

    return rtn


def get_list_chars_in_search_string(in_str):
    return list(set(in_str))


if __name__ == '__main__':
    print(find_substring("jad", "721jacjad23"))
    print(get_list_chars_in_search_string("yyy"))
