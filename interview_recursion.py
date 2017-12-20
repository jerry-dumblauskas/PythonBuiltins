def check_it_easy(in_x):
    return sum(range(in_x[-1] + 1)) - sum(in_x)


if __name__ == "__main__":
    x = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(check_it_easy(x))
    x = list(range(100))
    print(x)
    x.remove(55)
    print(x)
    print(check_it_easy(x))
