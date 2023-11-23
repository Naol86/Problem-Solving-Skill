for i in range(int(input())):
    x = input()
    x = x + "1"
    a = 0
    ans = []
    while( a < len(x) - 1):
        if x[a] != x[a+1]:
            if x[a] not in ans:
                ans.append(x[a])
            a+=1
        else:
            a+=2
    ans.sort()
    ans = "".join(ans)
    print(ans)