from collections import deque

x, m = map(int, input().split())
nums = [int(i) for i in input().split()]

nums = deque([(nums[i], i) for i in range(x)])

while nums:
  child, last = nums.popleft()
  if child - m > 0:
    nums.append((child - m, last))
print(last + 1)