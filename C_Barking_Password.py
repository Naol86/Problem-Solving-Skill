password = input()
ans = False
first = False
last = False
for i in range(int(input())):
  s = input()
  if s == password:
    ans = True
  if s[1] == password[0]:
    first = True
  if s[0] == password[1]:
    last = True
if ans or (first and last):
  print("YES")
else:
  print("NO")