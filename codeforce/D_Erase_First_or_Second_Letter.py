from collections import defaultdict
def solve():
  n = int(input())
  word = input().strip()
  
  last = defaultdict(lambda : n)
  last[word[-1]] = n-1
  ans = 1
  for i in range(n-2, -1, -1):
    ans += last[word[i]] - i
    # print(last[i],i)
    last[word[i]] = i
  print(ans)
  
for _ in range(int(input())):
  solve()