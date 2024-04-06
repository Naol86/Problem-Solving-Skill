for _ in range(int(input())):
  input()
  x, y = map(int, input().split())
  pointes = []
  for __ in range(y):
    a,b = map(int, input().split())
    pointes.append((b,a, __ + 1))
  # if y // 2 == x:
  #   print(sum([o[0] for o in pointes]))
  #   for i in range(y // 2):
  #     print(i + 1, y - i)
  #   print()
  #   continue

  pointes.sort()
  temp = pointes[:x*2]
  temp.sort(key = lambda x: x[1])
  print(sum([o[0] for o in temp]))
  # print(temp)
  for i in range(len(temp)//2):
    print(temp[i][2], temp[-(i + 1)][2])
  print()