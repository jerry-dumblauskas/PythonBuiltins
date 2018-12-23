def do_it_fast(in_int):
    return (1 + in_int) * in_int/2


def do_it_slow(in_int):
    x = 0
    for x1 in range(in_int + 1):
        x = x + x1
    return x

if __name__ == '__main__':
    import datetime
    in_number = pow(10,9)
    # FAST
    start_time = datetime.datetime.now()
    fast = do_it_fast(in_number)
    print(fast)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

    # SLOW
    start_time = datetime.datetime.now()
    slow = do_it_slow(in_number)
    print(slow)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
    print("the diff better be 0, and is", fast-slow)