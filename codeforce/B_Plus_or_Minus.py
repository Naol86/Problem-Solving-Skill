for _ in range(int(input())):
    lis = [int(i) for i in input().split()]
    if lis[0] + lis[1] == lis[2]:
        print("+")
    else:
        print("-")
