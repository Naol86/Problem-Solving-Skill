s = input().strip()
t = []
u = []

letters = [0] * 26

for char in s:
  letters[ord(char) - ord('a')] += 1

i = 0
while i < 26 and letters[i] == 0:
  i += 1
j = 0
while j < len(s):
  letters[ord(s[j]) - ord('a')] -= 1
  if i == ord(s[j]) - ord('a'):
    u.append(s[j])
    while i < 26 and letters[i] == 0:
      i += 1
  else:
    t.append(s[j])
  j += 1


u.extend(t[::-1])
print(''.join(u))

if len(s) != len(u):
  print(-1)

