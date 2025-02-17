last = ''
count = 0
for _ in range(int(input())):
  n = input()
  if len(last) == 0:
    last = n
  else:
    if last[-1] == n[0]:
      count += 1
  last = n
print(count + 1)