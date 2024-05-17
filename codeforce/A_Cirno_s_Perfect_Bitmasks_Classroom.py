for i in range(int(input())):
  x = int(input())
  xor = -1
  And = -1
  temp = x
  i = 0
  while xor == -1 or And == -1:
    if And == -1 and temp & 1:
      And = i
      if temp > 1:
        xor = -1
        break
    elif xor == -1 and temp & 1:
      break
    elif xor == -1 and temp & 1 == 0:
      xor = i
    temp >>= 1
    i += 1
  ans = 0
  if xor != -1:
    ans |= 1<<xor
  ans |= 1<<And
  # print(And, xor)
  print(ans)