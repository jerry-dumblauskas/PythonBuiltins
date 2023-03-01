import math
ans = list(str(math.factorial(100)))
ans = [int(i) for i in ans]
ans = int(math.fsum(ans))
print(ans)