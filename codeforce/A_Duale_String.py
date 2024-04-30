for _ in range(int(input())):
  x = input()
  if len(x) % 2 != 0:
    print("NO")
  else:
    if x[:len(x)//2] == x[len(x)//2:]:
      print("YES")
    else:
      print("NO")