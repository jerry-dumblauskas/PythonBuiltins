"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
a=1
b=2
c=3
for a in range(1, 1001):
    for b in range(a+1, 1001):
        for c in range(b+1, 1001):
            if (a + b + c) == 1000:
                if (a*a)+(b*b) == c*c:
                    print(f'a:{a} b:{b} c:{c}')
                    print(a*b*c)

