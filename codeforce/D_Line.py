for _ in range(int(input())):
    x = int(input())
    lis = input()
    temp = []
    _sum = 0
    for i in range(x):
        if lis[i] == 'L':
            _sum += i
            temp.append((i,x-i-1))
        else:
            _sum += x - i - 1
            temp.append((x-i-1,i))
    ans = []
    a = 0
    b = x - 1
    while a <= b:
        if temp[a][0] >= temp[a][1]:
            a += 1
        elif temp[b][0] >= temp[b][1]:
            b -= 1
        else:
            if (temp[a][1] - temp[a][0]) > (temp[b][1] - temp[b][0]):
                _sum += temp[a][1] - temp[a][0]
                ans.append(_sum)
                a += 1
            else:
                _sum += temp[b][1] - temp[b][0]
                ans.append(_sum)
                b -= 1
    leng = len(ans)
    temp = _sum
    while leng < x:
        ans.append(_sum)
        leng += 1
    print(*ans)