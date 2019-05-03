def setindex(strings):
    print('index processing begins')
    mid = strings + '$'
    str_list = []
    for i in range(len(strings)+1):
        str_list.append(str_rotate(i,mid))
    str_list = sorted(str_list)
    output =[]
    #print(str_list)
    for i in str_list:
        indexnum = len(strings) - i.index('$')
        output.append([i[0],i[-1],indexnum])
    #print(output)
    print('index success!')
    return output


def str_rotate(distance,strings):
    output = strings[distance:] + strings[0:distance]
    return output

#setindex('abracadabra')

def tally_convert(bwtindex):
    #initialize
    A,C,G,T = [0,0,0,0]
    A_head,C_head,G_head,T_head = [0,0,0,0]
    A_index, C_index, G_index, T_index = [0, 0, 0, 0]
    #loop
    for i in bwtindex:
        # Order : A C G T
        i.append([0,0,0,0])
        # Line LAST
        if i[1] == 'A':
            A += 1
        elif i[1] == 'C':
            C += 1
        elif i[1] == 'G':
            G += 1
        elif i[1] == 'T':
            T += 1
        #Line FRONT
        if i[0] == 'A':
            A_head += 1
        elif i[0] == 'C':
            C_head += 1
            if C_index == 0:
                C_index = A_head
        elif i[0] == 'G':
            G_head += 1
            if G_index == 0:
                G_index = A_head + C_head
        elif i[0] == 'T':
            T_head += 1
            if T_index == 0:
                T_index = A_head + C_head + G_head
        i[3] = [A,C,G,T]
    indexarray = [A_index,C_index,G_index,T_index]
    #print(bwtindex)
    #print(indexarray)
    return [bwtindex,indexarray]

#tally_convert(setindex('ACGTGTCAT'))

def tally_search(find,tally_matrix):
    print('search begins !')
    find = list(find)
    #print(find)
    ans = []
    for i in tally_matrix[0]:
        k = i
        while len(find) > 1:
            if k[0] == find[-1]:
                if k[1] == find[-2]:
                    if len(find) == 2:
                        ans.append(k[2])
                        break
                    find.pop()
                    if k[1] == 'A':
                        k = tally_matrix[0][tally_matrix[1][0]+ k[3][0]]
                    elif k[1] == 'C':
                        k = tally_matrix[0][tally_matrix[1][1]+ k[3][1]]
                    elif k[1] == 'G':
                        k = tally_matrix[0][tally_matrix[1][2]+ k[3][2]]
                    elif k[1] == 'T':
                        k = tally_matrix[0][tally_matrix[1][3]+ k[3][3]]
                else:
                    break
            else:
                break
    #print(ans)
    print('Well done !')
    return ans

def show(string,search,ans):
    for i in range(len(ans)):
        print('This is NO.%s alignment answer' % str(i+1))
        print(string)
        for j in range(ans[i]-1):
            print('',end = ' ')
        print (search,end='')
        print('')
        print('')





refstring = 'ACGTGTCAT'
search = 'GT'

show(refstring , search,tally_search(search,tally_convert(setindex(refstring))))