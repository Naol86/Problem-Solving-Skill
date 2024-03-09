x = int(input())
nums = [int(i) for i in input().split()] + [0]
stack = [(-1,-1)]
ans = [0] * x
ite = []
for index, val in enumerate(nums):
    while len(stack) > 1 and stack[-1][0] > val:
        ite.append((stack[-1][0], (stack[-1][1] - stack[-2][1]) * (index - stack[-1][1])))
        stack.pop()
    stack.append((val, index))

ite.sort(reverse=True)

# print(ite)
_min = 0
for i, j in ite:
    j = j if j < x else x
    for index in range(_min, j):
        ans[index] = i
    _min = max(_min, j)

print(*ans)

