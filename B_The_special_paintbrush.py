for _ in range(int(input())):
  x = input()
  s = input()
  first = None
  last = None
  for i in range(len(s)):
    c = s[i]
    if c == 'B':
      last = i
      if first == None:
        first = i
  
  if first is None and last is None:
    print(0)
  else:
    print(last - first + 1)