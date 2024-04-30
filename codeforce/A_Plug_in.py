x = input()

stack = []

i = 0
while i < len(x):
  if stack and stack[-1] == x[i]:
    stack.pop()
  else:
    stack.append(x[i])
  i += 1
print(''.join(stack))