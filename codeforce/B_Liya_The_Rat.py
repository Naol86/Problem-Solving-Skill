lis = input()
leng = len(lis)

temp = []
for _ in range(int(input())):
    x = [int(i) for i in input().split()]
    temp.append(x)


pre = 0
_sum = [0] * leng
for i in range(1, leng):
    if lis[i] == lis[i - 1]:
        pre += 1
    _sum[i] = pre

for x, y in temp:
    print(_sum[y-1] - _sum[x-1])
