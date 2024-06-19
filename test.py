worker = [2,4,6,8,9,10]
pro = [3,4,7,9,10,11]

lower = 0
upper = 0

_max = 0

# while lower < len(pro):
for lower in range(len(pro)):
    while upper < len(worker):
        if worker[upper] <= pro[lower]:
            upper += 1
        else:
            break
    print(pro[lower],"will work on",worker[upper-1])
    _max = max(_max, profit[upper-1])
    ans += _max
