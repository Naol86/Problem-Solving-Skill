count = 0
for i in range(int(input())):
    lis = [int(j) for j in input().split()]
    if sum(lis) > 1:
        count += 1
print(count)