w, e = map(int, input().split())

r, b = w, e
hash = {0:r, 1:b}
# print(hash)
def solve(j):
  x, y = 0, 0
  last = None
  i = 0
  while hash[0] or hash[1]:
    # print(hash, last)
    # print(last, i, hash.get(last))
    if last is None:
      if hash[j]:
        hash[j] -= 1
        last = j
      else:
        last = (j+1)%2
        hash[last] -= 1
    elif (i % 2) == 0:
      # print(hash[last])
      if hash[last]:
        hash[last] -= 1
        x += 1
      else:
        hash[(last + 1)%2] -= 1
        last = (last + 1)%2
        y += 1
    else:
      # print(hash[(last + 1)%2])
      if hash[((last + 1)%2)]:
        hash[(last + 1)%2] -= 1
        last = (last + 1)%2
        y += 1
      else:
        hash[last] -= 1
        x += 1
    # print(last)
    i += 1
  return x, y

ans = solve(0)
# print(ans)

r, b = w, e
hash = {0:r, 1:b}
ans2 = solve(1)
if ans[0] - ans[1] > ans2[0] - ans2[1]:
  print(*ans)
else:
  print(*ans2)
# print(solve(1))
