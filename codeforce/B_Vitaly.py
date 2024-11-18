x = int(input())
nums = [int(i) for i in input().split()]
pos = []
neg = []
zero = []

for num in nums:
  if num == 0:
    zero.append(num)
  elif num < 0:
    neg.append(num)
  else:
    pos.append(num)

if pos == []:
  a = neg.pop()
  b = neg.pop()
  pos.append(a)
  pos.append(b)
if len(neg) % 2 == 0:
  a = neg.pop()
  zero.append(a)
print(len(neg), *neg)
print(len(pos), *pos)
print(len(zero), *zero)