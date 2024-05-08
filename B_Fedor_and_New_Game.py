n, m, k = map(int, input().split())

nums = []
for _ in range(m + 1):
  nums.append(int(input()))

count = 0
i = 0
while i < m:
  temp = nums[-1] ^ nums[i]
  length = 0
  while temp > 0:
    if temp & 1 == 1:
      length += 1
    temp >>= 1
  # temp = temp.bit_count()
  if length <= k:
    count += 1
  i += 1
print(count)