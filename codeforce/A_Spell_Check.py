dic = {"T":1,'i':1,'m':1,'u':1,'r':1}
for i in range(int(input())):
    x = int(input())
    lis = input()
    if x > 5:
        print("NO")
        continue
    temp = {}
    for j in lis:
        if j not in temp:
            temp[j] = 1
        else:
            temp[j] += 1
    if temp == dic:
        print("YES")
    else:
        print("NO")