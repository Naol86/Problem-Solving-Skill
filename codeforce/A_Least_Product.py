for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    pro = 1
    for i in lis:
        pro *= i
    # print(lis, pro)
    if pro <= 0:
        print(0)
    else:
        print(1)
        print(1,0)