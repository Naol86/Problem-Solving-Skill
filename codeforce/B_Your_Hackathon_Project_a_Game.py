n, m = map(int, input().split())
nums = [int(i) for i in input().split()]
sums1 = [0]
sums2 = [0]
for i in range(1, n):
  if nums[i] >= nums[i - 1]:
    sums1.append(0)
  else:
    sums1.append(nums[i-1] - nums[i])

  if nums[-i - 1] >= nums[-i]:
    sums2.append(0)
  else:
    sums2.append(nums[-i] - nums[-i - 1])

sums2.reverse()
# print(sums2)

for i in range(1, len(sums1)):
  sums1[i] += sums1[i - 1]
  sums2[-i-1] += sums2[-i]

# print(sums1)
# print(sums2)
for _ in range(m):
  x, y = map(int, input().split())
  if x < y:
    print(sums1[y - 1] - sums1[x -1])
  else:
    print(sums2[y - 1] - sums2[x - 1])