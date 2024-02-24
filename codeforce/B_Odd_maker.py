for _ in range(int(input())):
    leng, query = [int(i) for i in input().split()]
    lis = [0] + [int(i) for i in input().split()]
    for i in range(1,leng + 1):
        lis[i] = lis[i] + lis[i - 1]

    temp = []
    for _ in range(query):
        l, r, k = [int(i) for i in input().split()]
        temp.append((l,r,k))

    for l, r, k in temp:
        cache = lis[-1] - lis[r] - lis[l - 1]
        cache += (k * (r - l + 1))

        if cache % 2 == 0:
            print("NO")
        else:
            print("YES")
            
