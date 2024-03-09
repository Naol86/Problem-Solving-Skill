count = 0
stack = []
current = 1
for _ in range(2 * int(input())):
    command = input().split()
    if command[0] == 'add':
        stack.append(int(command[1]))
    else:
        if len(stack) == 0:
            pass
        elif stack[-1] == current:
            stack.pop()
        else:
            count += 1
            stack = []
        current += 1
print(count)