for _ in range(int(input())):
    a, b = map(int, input().split())
    aau = {1,2,3,4}
    aastu = {5,6,7}
    astu = {8, 9}
    ans = "Yes"
    if a in aau and b in aau:
        print(ans)
    elif a in aastu and b in aastu:
        print(ans)
    elif a in astu and b in astu:
        print(ans)
    else:
        print('No')