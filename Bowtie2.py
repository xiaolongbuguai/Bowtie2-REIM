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


def str_rotate(distance,strings):
    output = strings[distance:] + strings[0:distance]
    return output

setindex('abracadabra')
