s = input()

vowels = []
vol = set(['A','E','O','I','U','Y'])

for i in range(len(s)):
  if s[i] in vol:
    vowels.append(i)
vowels.append(len(s))
_max = vowels[0] + 1

for i in range(len(vowels) - 1):
  _max = max(_max, vowels[i+1] - vowels[i])
print(_max)