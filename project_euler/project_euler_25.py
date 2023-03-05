cache_it = {}


def fib(in_num):
    if in_num in (1, 2):
        return 1
    if cache_it.get(in_num):
        return cache_it[in_num]

    rtn = fib(in_num - 1) + fib(in_num - 2)
    if not cache_it.get(in_num):
        cache_it[in_num] = rtn
    return rtn


if __name__ == '__main__':
    for i in range(1, 10000):
        answer = fib(i)
        print(f'{i} : {len(str(answer))}')
        if len(str(answer)) == 1000:
            break
