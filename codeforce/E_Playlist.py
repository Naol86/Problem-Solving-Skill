n, k = map(int, input().split())

nums = []
for _ in range(n):
  a, b = map(int, input().split())
  nums.append((b, a))
nums.sort()
# print(nums)
i = 0
right = 0
_sum = 0
ans = 0
while right < n and i < n:
  _sum += nums[right][1]
  if right >= k:
    _sum -= nums[i][1]
    i += 1
  # print(nums[right], _sum)
  if i < n:
    ans = max(ans, _sum * nums[i][0])
  if right == n - 1:
    _sum -= nums[right][1]
    continue
  right += 1
print(ans)