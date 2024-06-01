for _ in range(int(input())):
  n = int(input())
  w = input().strip()
  word = [i for i in set(w)]
  word.sort()
  
  res = []
  r = len(word) - 1
  nx = {}
  for i in range(len(word)):
    nx[word[i]] = word[r]
    r -= 1
  for i in range(n):
    res.append(nx[w[i]])
  print("".join(res))