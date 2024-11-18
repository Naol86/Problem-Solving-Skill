a, b = map(int, input().split())

nums = [a]
def back_track(b, current):
  if current > b:
    return False
  if current == b:
    return True
  nums.append(nums[-1] * 2)
  x = back_track(b, current * 2)
  if x:
    return True
  nums.pop()
  nums.append(nums[-1] * 10 + 1)
  x = back_track(b, current * 10 + 1)
  if x:
    return True
  nums.pop()
  return False

if a > b or not back_track(b, a):
  print('NO')
else:
  print('YES')
  print(len(nums))
  print(*nums)