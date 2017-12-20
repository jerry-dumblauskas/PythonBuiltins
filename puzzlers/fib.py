import time


def fib(in_num):
    if in_num in (1, 2):
        return 1

    return fib(in_num - 1) + fib(in_num - 2)


if __name__ == '__main__':
    start = time.time()
    print(fib(37))
    end = time.time()
    print(end - start)
