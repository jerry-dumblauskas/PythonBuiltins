longest_sequence = 0
starting_number = 0
for i in range(2,1000000):
    l_starting_num = i
    l_seq = 0
    while True:
        l_seq += 1
        if i == 1:
            if l_seq > longest_sequence:
                longest_sequence = l_seq
                starting_number = l_starting_num
            break
        if i % 2 == 0:
            i = i/2
        else:
            i = 3*i + 1

print (longest_sequence)
print (starting_number)