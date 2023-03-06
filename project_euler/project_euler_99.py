import csv
import decimal
from decimal import Decimal
import math
with open("p099_base_exp.txt") as dta:
    fle = csv.reader(dta)
    greatest = 0.0
    l_cnt = 0
    for cnt, item in enumerate(fle):
        l_base = decimal.Decimal(math.sqrt(decimal.Decimal(item[0])))
        l_exp = decimal.Decimal(math.sqrt(decimal.Decimal(item[1])))
        tst = Decimal.__pow__(l_base, l_exp)
        if tst > greatest:
            greatest = tst
            l_cnt = cnt


print(math.pow(greatest, 2))
print(l_cnt)
