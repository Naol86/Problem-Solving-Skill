

for _ in range(int(input())):
  coin = int(input())
  nums = [5, 3, 1]
  ans = [coin]
  memo = set()
  def dp(left, one):
    if left < 0:
      return
    if (left, one) in memo:
      return
    memo.add((left, one))
    if left == 0:
      ans[0] = min(ans[0], one)
    for num in nums:
      if num == 1:
        one += 1
      dp(left - num, one)
  dp(coin, 0)
  print(ans[0])