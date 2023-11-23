x = [int(i) for i in input().split()]
y = x[1]
lis = [int(i) for i in input().split()][:x[0]]
ans = 0
while(sum(lis) != y*len(lis)):
    increased = [y]
    for i in range(len(lis)):
        if lis[i] not in increased:
            increased.append(lis[i])
            lis[i] = lis[i] +1
    ans+=1
print(ans)