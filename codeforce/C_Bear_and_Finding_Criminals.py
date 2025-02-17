n, a = map(int, input().split())
nums = [int(i) for i in input().split()]

count = nums[a-1]
left = a - 2
right = a



while right < len(nums) or left >= 0:
  temp = 0
  if right < len(nums):
    temp += nums[right]
  else:
    temp += 10
  if left >= 0:
    temp += nums[left]
  else:
    temp += 10
  if temp == 2:
    count += 2
  elif temp < 2 or temp == 10:
    count += 0
  else:
    count += 1
  left -= 1
  right += 1
print(count)
