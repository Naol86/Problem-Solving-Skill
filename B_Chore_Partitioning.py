n, a, b = map(int, input().split())
nums = [int(i) for i in input().split()]
nums.sort()
print(nums[-a] - nums[-a-1])