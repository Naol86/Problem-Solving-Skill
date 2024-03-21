for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    if x == 1 and y == 1:
        print("YES")
        continue
    if x == y:
        print("YES")
        continue
    if x % 3 != 0 or x < y:
        print("NO")
        continue
    target = y
    stack = [x]
    _set = set(stack)
    while stack:
        temp = stack.pop()
        _set.remove(temp)
        a = temp // 3
        b = a * 2
        if a == target or b == target:
            print("YES")
            break
        if a > target and a % 3 == 0 and a not in _set:
            stack.append(a)
            _set.add(a)
        if b > target and b % 3 == 0 and b not in _set:
            stack.append(b)
            _set.add(b)
    else:
        print("NO")