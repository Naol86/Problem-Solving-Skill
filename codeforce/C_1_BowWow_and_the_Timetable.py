x = [i for i in input()]

count = 0
i = len(x) - 1
one = 0
while i > 0:
  if x[i] == '1':
    one = 1
  if x[i-1] == '1':
    one = 1
  i -= 2
  count += 1

if i == 0:
  print(count + one)
else:
  print(count)
