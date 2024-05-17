
from typing import Counter


for _ in range(int(input())):
  s = input()
  count = Counter(s)
  if len(count) == 1:
    print("NO")
  else:
    print("YES")
    e = s[0]
    for i in range(1, len(s)):
      if s[i] != e:
        break
    print(s[i:] + s[:i])