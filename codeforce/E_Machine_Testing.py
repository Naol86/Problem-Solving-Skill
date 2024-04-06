import math


for _ in range(int(input())):
    n = int(input())
    health = [int(i) for i in input().split()]
    power = [int(i) for i in input().split()]

    stack = [[float('inf'), power[0]]]
    i = 1
    ans = 0
    while i < n:
        current = 0
        while stack and health[i] > 0:
            top_time = stack[-1][0]
            top_power = stack[-1][1]
            time_took = math.ceil(health[i]/top_power)
            if time_took <= top_time:
                ans = max(ans, time_took + current)
                stack[-1][0] -= time_took
                if stack[-1][0] <= 0:
                    stack.pop()
                stack.append([time_took + current, power[i]])
                break
            else:
                current += top_time
                health[i] -= top_time * top_power
                stack.pop()
            # print(stack, current, ans)
            ans = max(ans, current)
        i += 1
        # print(ans, stack, current)
        ans = max(ans, current)
    print(ans)