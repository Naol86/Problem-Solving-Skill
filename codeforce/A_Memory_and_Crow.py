x = int(input())
nums = [int(i) for i in input().split()]

odd_sum = -nums[-1]
even_sum = nums[-1]

even = True

ans = [nums[-1]]
for i in range(x-2, -1, -1):
  if even:
    ans.append(even_sum + nums[i])
    even_sum -= ans[-1]
    odd_sum += ans[-1]
  else:
    ans.append(odd_sum + nums[i])
    even_sum += ans[-1]
    odd_sum -= ans[-1]
  even = not even
print(*ans[::-1])