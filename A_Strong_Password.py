for _ in range(int(input())):
  s = [i for i in input()]
  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      if s[i] != 'a':
        ans = s[:i] + ['a'] + s[i:]
      else:
        ans = s[:i] + ['b'] + s[i:]
      print(''.join(ans))
      break
  else:
    if s[-1] != 'a':
      ans = s + ['a']
    else:
      ans = s + ['b']
    print(''.join(ans))
    