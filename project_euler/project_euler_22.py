mapper = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

dta = open("p022_names.txt")
new_dta = []
for item in dta:
    new_dta = [i for i in item.split(",")]

final = sorted([i[1:-1] for i in new_dta])

cnt = 1
ans = 0
for name in final:
    the_sum = 0
    for item in name:
        the_sum += mapper[item]
    ans = ans + (cnt * the_sum)
    cnt += 1
print(ans)

