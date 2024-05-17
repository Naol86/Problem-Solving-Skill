from collections import Counter


for _ in range(int(input())):
  s = [int(i) for i in input()]
  # s.append((s[-1] + 1)%2)
  count = Counter(s)
  if len(count) == 1:
    print(1)
  else:
    count = 0
    pre = s[0]
    check = 0
    for i in range(len(s)):
      if s[i] != pre:
        count += 1
        if pre == 0:
          check = 1
        pre = s[i]
    print(count - check + 1)