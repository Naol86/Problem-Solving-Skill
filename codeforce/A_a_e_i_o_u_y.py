x = int(input())
s = input()
stack = []
vowels = {'a', 'i', 'e', 'o', 'u', 'y'}

ans = []

for i in s:
  if i in vowels:
    if stack and stack[-1] in vowels:
      continue
    else:
      stack.append(i)
  else:
    stack.append(i)
  # while stack and stack[-1] in vowels
print(''.join(stack))