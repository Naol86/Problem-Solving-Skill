s = input()
x = int(input())
if len(s) < x:
  print("impossible")
else:
  count = 0
  letters = set()
  for i in s:
    if i not in letters:
      letters.add(i)
      count += 1
  
  if x - count < 0:
    print(0)
  else:
    print(x - count)