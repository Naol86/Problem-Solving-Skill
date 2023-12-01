for i in range(int(input())):
    x = [int(j) for j in input().split()]
    lis = [int(j) for j in input().split()]
    _max_peak = 0
    _min_index = 1
    _no_peak = 0
    for j in range(1,x[1]-1):
        if lis[j] > lis[j-1] and lis[j] > lis[j+1]:
            _max_peak+=1
            _no_peak +=1
            _min_index = 1
    a = 0
    b = x[1]
    while b < len(lis):
        if lis[a+1] > lis[a] and lis[a+1]>lis[a+2]:
            _no_peak-=1
        if lis[b-1] > lis[b] and lis[b-1] > lis[b-2]:
            _no_peak+=1
            if _no_peak > _max_peak:
                _max_peak = _no_peak
                _min_index = a+2
        a+=1
        b+=1
    print(_max_peak+1,_min_index)