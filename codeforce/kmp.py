x = input()

kmp = [0] * len(x)

# kmp algorithm

i = 0
j = 1
while j < len(x):
  if x[i] == x[j]:
    kmp[j] = i + 1
    i += 1
    j += 1
  elif i == 0:
    j += 1
  else:
    i = kmp[i - 1]

print(kmp)