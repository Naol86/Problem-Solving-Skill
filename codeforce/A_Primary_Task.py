for _ in range(int(input())):
  x = input()
  if len(x) < 3:
    print("NO")
    continue
  y = int(x[2:])
  # print(x[:2])
  if int(x[:2]) == 10 and x[2] != '0' and y > 1:
    print("YES")
  else:
    print("NO")