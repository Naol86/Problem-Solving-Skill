for _ in range(int(input())):
    x = int(input())
    nums = [int(i) for i in input().split()]
    stack = []
    _min = 0
    for num in nums:
        if not stack:
            stack.append(num)
        else:
            temp = stack[-1] - _min
            stack[-1] = _min
            if stack[-1] >= num + temp:
                print("NO")
                break
            stack.append(num + temp)
            _min += 1
    else:
        print("YES")