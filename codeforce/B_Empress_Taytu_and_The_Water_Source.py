import math


for _ in range(int(input())):
    n, hour = [int(i) for i in input().split()]
    demand = [int(i) for i in input().split()]
    time = [int(i) for i in input().split()]
    _sum = sum(time)
    if _sum > hour:
        print(-1)
        continue
    if _sum == hour:
        print(max(demand))
        continue
    def calculate_hour(mid):
        count = 0
        for i in range(n):
            count += math.ceil(demand[i] / mid) * time[i]
        return count
    _min = demand[0]
    _max = demand[0]
    for i in demand:
        _min = min(_min, i)
        _max = max(_max, i)
    left = 1
    right = _max
    ans = _max
    # print(_min, _max, ans)
    
    while left <= right:
        mid = left + (right - left) // 2
        temp = calculate_hour(mid)
        # print(mid, temp, 'i am temp')
        if temp <= hour:
            if mid <= ans:
                ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1
    print(ans)