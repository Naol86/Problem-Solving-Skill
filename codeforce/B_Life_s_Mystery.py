s = input()
stack = []
for i in s:
    if not stack:
        stack.append(i)
    elif stack and stack[-1] == i:
        stack.pop()
    else:
        stack.append(i)
print(''.join(stack))