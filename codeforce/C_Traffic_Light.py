for i in range(int(input())):
    z = [j for j in input().split()][:2]
    lis = input()
    ans = 0
    a = 0
    check = False
    count = 0
    end = False
    while a < int(z[0]):
        if lis[a] == z[1] and check == False:
            check = True
        elif check:
            if lis[a] == "g":
                ans = max(ans, count)
                if end == True:
                    a = len(lis)
                    break
                check = False
                count = 0
                a+=1
            else:
                count +=1
                a+=1
            if a == int(z[0]):
                a = 0
                end = True
        else:
            a+=1
    print(ans)