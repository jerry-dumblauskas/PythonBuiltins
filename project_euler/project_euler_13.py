dta = open("f_13.txt")

answer = 0
for row in dta:
    row = int(row.strip())
    answer += row
print(str(answer)[:10])
