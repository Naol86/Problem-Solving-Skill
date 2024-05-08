x = int(input())
lis = []
for i in range(x):
  temp = [int(i) for i in input().split()]
  temp.sort()
  temp.append(i)
  lis.append(temp)

lis.sort(reverse=True)

_max = lis[0][0]
hash = {}
ans = [lis[0][-1]+1]
for i in range(x):
  if tuple(lis[i][1:-1]) in hash and lis[i][0] + hash[tuple(lis[i][1:-1])][0] > _max:
    _max = lis[i][0] + hash[tuple(lis[i][1:-1])][0]
    ans = [hash[tuple(lis[i][1:-1])][-1] + 1, i + 1]
    if hash[tuple(lis[i][1:-1])][0] < lis[i][0]:
      hash[tuple(lis[i][1:-1])] = [lis[i][0], i]
  else:
    tt = tuple(lis[i][1:-1])
    if tt not in hash:
      hash[tt] = [lis[i][0], i]
    else:
      if hash[tuple(lis[i][1:-1])][0] < lis[i][0]:
        hash[tuple(lis[i][1:-1])] = [lis[i][0], i]
# print(ans, _max)
# print(hash)
ans.sort()
print(len(ans))
print(*ans)