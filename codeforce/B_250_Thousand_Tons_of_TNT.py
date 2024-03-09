for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    lis.sort()
    print(lis)
    print(lis[-1] - lis[0])