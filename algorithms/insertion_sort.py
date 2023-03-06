import time

lst = [5, 2, 4, 6, 1, 3]


def insertion_sort(in_seq):
    for j in range(1, len(in_seq)):
        l_key = in_seq[j]
        i = j - 1
        while i >= 0 and in_seq[i] > l_key:
            in_seq[i + 1] = in_seq[i]
            i = i - 1
        in_seq[i + 1] = l_key


if __name__ == '__main__':
    start = time.time()
    insertion_sort(lst)
    end = time.time()
    print(lst)
    print(end - start)
