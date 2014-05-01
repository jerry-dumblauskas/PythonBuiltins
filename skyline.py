__author__ = 'jerrydumblauskas'

def calc_skyline(in_lst):
    rtn = [] # hor, vert
    prev_high_water_mark = [0,0,0] #lft, hgt, rgh
    l_first = True
    for tup in in_lst:
        if l_first:
            l_first = False
            rtn.append(tup[0])
            rtn.append(tup[1])
            prev_lst = list(tup)
            continue
        '''
        now check the prev lst and update values

        '''
        if tup[0] > prev_high_water_mark[0]:
            pass


    return rtn

def break_into_chunks(in_lst):
    '''
    Let's separate the data into chunks
    [(1,2,3),(2,3,4),(7,8,9)]
    to
    [[(1,2,3),(2,3,4)],[(7,8,9)]
    '''
    rtn_lst = []
    chunk_lst = []
    fst = True
    right_edge = 0
    add_last = False
    print in_lst

    for tup in in_lst:
        if fst:
            fst = False
            chunk_lst.append(tup)
            right_edge = tup[2]
            continue
        if tup[0] > right_edge:
            rtn_lst.append(chunk_lst)
            chunk_lst = []
            add_last = False
        else:
            add_last = True
        if tup[2] > right_edge:
            right_edge = tup[2]

        chunk_lst.append(tup)
    if add_last:
        rtn_lst.append(chunk_lst)

    return  rtn_lst

if __name__ == '__main__':
    #print calc_skyline([(1,11,5),(2,6,7),(3,13,9),(12,7,16),(14,3,25),(19,18,22),(23,13,29),(24,4,28)])
    #print (1,11,3,13,9,0,12,7,16,3,19,18,22,3,23,13,29,0)
    print break_into_chunks([(1,11,5),(2,6,7),(3,13,9),(12,7,16),(14,3,25),(19,18,22),(23,13,29),(24,4,28)])
