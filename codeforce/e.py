for _ in range(int(input())):
  x = int(input())
  s = [i for i in input()]
  if x == 1:
    print(s[0])
    continue
  temp = s[1:]
  temp.sort()
  # print(temp)
  if temp[0] > s[0]:
    print(''.join(s))
  else:
    for i in range(x - 1, 0, -1):
      if s[i] == temp[0]:
        s[i] = ""
        break
    print(f"{temp[0]}{''.join(s)}")
  # print(temp)