__author__ = 'jerrydumblauskas'

# for a brain teaser problem -- will grab the url later

def calc_skyline2(in_lst):
    '''
    in_lst = [(1,11,5),(2,6,7),(3,13,9)]
    rtn (1,11,3,13,9,0,12,7,16,3,19,18,22,3,23,13,29,0)
    '''
    rtn = [] # hor, vert
    stack_lst = []
    m_len = 0
    '''
    build data structure

    '''
    for tup in in_lst:
        if m_len < tup[2]:
            m_len = tup[2]
    for _ in range(m_len + 2):
        stack_lst.append([0])

    '''
    load data structure
    stack_lst will be a list of lists, each position will
    have at least 2 entries, a max and a min and if there is a change
    in maxes between positions, we will go down to the min, or where there is
    a match
    '''
    for tup in in_lst:
        for x in range(tup[0], tup[2] + 1):
                stack_lst[x].append(tup[1])

    '''
    analyze data and return result
    '''
    for x in range(1, len(stack_lst)):
        if max(stack_lst[x]) > max(stack_lst[x-1]):
            rtn.append(x)
            rtn.append(max(stack_lst[x]))
        elif max(stack_lst[x]) < max(stack_lst[x-1]):
            rtn.append(x-1)
            rtn.append(poop(stack_lst[x-1], stack_lst[x]))
            if max(stack_lst[x]) > poop(stack_lst[x-1], stack_lst[x]):
                rtn.append(x)
                rtn.append(max(stack_lst[x]))
    return tuple(rtn)

def poop(lst1, lst2):
    lst1_s = sorted(lst1, reverse=True)
    lst1_s.pop()
    for l_val in lst1_s:
        if l_val in lst2:
            return l_val
    return  0

def calc_skyline(in_lst):
    '''
    (1,11,3,13,9,0,12,7,16,3,19,18,22,3,23,13,29,0)
    '''
    rtn = [] # hor, vert

    for lsts in break_into_chunks(in_lst):
        fst = True
        hgt = 0
        rght = 0
        for tup in lsts:
            if fst:
                fst = False
                rtn.append(tup[0])
                rtn.append(tup[1])
                hgt = tup[1]
                rght = tup[2]
                continue
            if (tup[1] > hgt):
                hgt = tup[1]
                rtn.append(tup[0])
            if (tup[2] > rght):
                rght = tup[2]


    return tuple(rtn)

def break_into_chunks(in_lst):
    '''
    Let's separate the data into chunks
    [(1,2,3),(2,3,4),(7,8,9)]
    to
    [[(1,2,3),(2,3,4)],[(7,8,9)]
    '''
    chunk_lst = []
    fst = True
    right_edge = 0

    for tup in in_lst:
        if fst:
            fst = False
            chunk_lst.append(tup)
            right_edge = tup[2]
            continue
        if tup[0] > right_edge:
            yield chunk_lst
            chunk_lst = []

        if tup[2] > right_edge:
            right_edge = tup[2]

        chunk_lst.append(tup)
    if chunk_lst:
        yield chunk_lst

if __name__ == '__main__':
    #print "[(1,11,5),(2,6,7),(3,13,9),(12,7,16),(14,3,25),(19,18,22),(23,13,29),(24,4,28)]"
    print (1,11,3,13,9,0,12,7,16,3,19,18,22,3,23,13,29,0)
    print calc_skyline2([(1,11,5),(2,6,7),(3,13,9),(12,7,16),(14,3,25),(19,18,22),(23,13,29),(24,4,28)])
    #for x in break_into_chunks([(1,11,5),(2,6,7),(3,13,9),(12,7,16),(14,3,25),(19,18,22),(23,13,29),(24,4,28)]):
     #   print x
