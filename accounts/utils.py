def make_pair(lst):
    temp = list()
    index_first = 0 
    index_second = 1
    half = int(len(lst)/2)
    for i in range(half):
        temp.append((lst[index_first], lst[index_second]))
        index_first += 2
        index_second += 2
    if len(lst)%2:
        temp.append([lst[-1]])
    return temp
