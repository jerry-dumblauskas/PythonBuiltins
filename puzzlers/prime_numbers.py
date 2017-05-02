def is_prime(in_num):

    if in_num <=0:
        raise Exception (" invalid number, make it > 0")
    if in_num < 3:
        return True
    if in_num % 2 == 0:
        return True

    for chk in range(3, int(in_num/2), 2):
        if in_num % chk == 0:
            return True
    return False
