from collections import deque

x, y = [int(i) for i in input().split()]
lis = [int(i) for i in input().split()]
nums = deque(lis)
query = []
ans = set()
_max = 0
for i in range(y):
    temp = int(input())
    _max = max(_max, temp)
    query.append(temp)
    ans.add(temp)

_max = max(lis)
_dict = {}
i = 0
while nums[0] != _max:
    a = nums.popleft()
    b = nums.popleft()
    if a > b:
        nums.appendleft(a)
        nums.append(b)
    else:
        nums.appendleft(b)
        nums.append(a)
    i += 1
    _dict[i] = (a, b)
i += 1

nums.popleft()
for j in query:
    if j < i :
        print(*_dict[j])
    else:
        print(_max, nums[(j - i) % (x - 1)])