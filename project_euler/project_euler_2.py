def fib(in_num):
    if in_num == 1:
        return 1
    if in_num == 2:
        return 2

    return fib(in_num - 1) + fib(in_num - 2)


if __name__ == '__main__':
    ans = 0
    for i in range(1, 40):
        tst = fib(i)

        if tst >= 4000000:
            break
        if tst % 2 == 0:
            ans += tst

    print(ans)