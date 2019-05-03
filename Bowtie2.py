def setindex(strings):
    print('index processing begins')
    mid = strings + '$'
    str_list = []
    for i in range(len(strings)+1):
        str_list.append(str_rotate(i,mid))
    str_list = sorted(str_list)
    output =[]
    print(str_list)
    for i in str_list:
        indexnum = len(strings) - i.index('$')
        output.append([i[0],i[-1],indexnum])
    print(output)
    return output


def str_rotate(distance,strings):
    output = strings[distance:] + strings[0:distance]
    return output

#setindex('abracadabra')

def tally_convert(bwtindex):
    #initialize
    A = 0
    C = 0
    T = 0
    G = 0
    for i in bwtindex:
        # Order : A C T G
        i.append([0,0,0,0])
        if i[1] == 'A':
            A += 1
        elif i[1] == 'C':
            C += 1
        elif i[1] == 'T':
            T += 1
        elif i[1] == 'G':
            G += 1
        i[3] = [A,C,T,G]
    print(bwtindex)

tally_convert(setindex('ATGCGTANNGTC'))

def tally_search():
