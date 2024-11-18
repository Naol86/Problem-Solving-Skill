from collections import Counter


for _ in range(int(input())):
  x = input()
  count = Counter(x)
  ans = 0
  for hey, val in count.items():
    if val >= 2:
      ans += 2
    else:
      ans += 1
  print(ans//2)