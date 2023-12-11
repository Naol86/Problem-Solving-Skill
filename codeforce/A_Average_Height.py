for i in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()][:x]
    odd = []
    even = []
    for j in lis:
        if j % 2 == 0:
            even.append(j)
        else:
            odd.append(j)
    for j in odd:
        print(j, end=" ")
    for j in even:
        print(j, end=" ")
    print()