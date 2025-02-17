



# 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# 1 1 0 0 0 0 0 1 1  0 0  0  1  0

# 1 1 0 0 0 1 0 1 1  0 0  0  1  0 
# 
# i = 6
# 3 = i - 3
# 4 = i - 2
# 5 = i - 1
# 6 = i - 0








for _ in range(int(input())):
  s = [i for i in input()]
  q = int(input())
  hash = set()
  for i in range(len(s)):
    if s[i:i+4] == ['1', '1', '0', '0']:
      hash.add(i)
  for _ in range(q):
    index, val = map(int, input().split())
    index -= 1
    start = max(index - 3, 0)
    end = index
    # print(index, s)
    s[index] = str(val)
    for i in range(start, end + 1):
      if s[i:i+4] == ['1', '1', '0', '0']:
        hash.add(i)
      else:
        if i in hash:
          hash.remove(i)
    if len(hash):
      print("YES")
    else:
      print("NO")