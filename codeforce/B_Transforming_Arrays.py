for _ in range(int(input())):
    x = int(input())
    lis_a = [int(i) for i in input().split()]
    lis_b = [int(i) for i in input().split()]
    
    if lis_a[0] != lis_b[0]:
        print("NO")
    else:
        hash = set([lis_a[0]])
        for i in range(1, x):
            if lis_a[i] > lis_b[i]:
                if -1 not in hash:
                    print("NO")
                    break
            elif lis_a[i] < lis_b[i]:
                if 1 not in hash:
                    print("NO")
                    break
            hash.add(lis_a[i])
        else:
            print("YES")
