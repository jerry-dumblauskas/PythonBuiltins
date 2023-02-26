"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def is_prime(in_num):
    if in_num <= 0:
        raise Exception(" invalid number, make it > 0")
    if in_num < 3:
        return True
    if in_num % 2 == 0:
        return False

    for chk in range(3, int(in_num / 2), 2):
        if in_num % chk == 0:
            return False
    return True


the_number = 2
cnt = 1
while cnt < 10002:
    if is_prime(the_number):
        print(str(the_number) + " is prime number:" + str(cnt))
        cnt+=1
    the_number+=1
