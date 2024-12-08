from collections import Counter


x ,y = map(int, input().split())

nums1 = [int(i) for i in input().split()]
nums2 = [int(i) for i in input().split()]

count1 = Counter(nums1)
count2 = Counter(nums2)

ans = 0

for key, value in count1.items():
  ans += (value * count2[key])

print(ans)