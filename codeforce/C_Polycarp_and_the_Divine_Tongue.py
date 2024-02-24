for _ in range(int(input())):
    s = input()
    point = 0
    count = 0
    stack_v = 0
    while point < len(s):
        if s[point] == 'w':
            count += 1
            stack_v = 0
        else:
            if stack_v == 1:
                count += 1
                stack_v -= 1
            else:
                stack_v += 1
        point += 1
    print(count)