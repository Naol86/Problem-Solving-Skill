x = int(input())
nums1 = [int(i) for i in input().split()]
nums2 = [int(i) for i in input().split()]

_max = 0
_sum = 0
for i in range(x):
  _sum += (nums1[i])

# print(_max, _sum)
nums2.sort()

if len(nums2) == 0:
  _max = 0
elif len(nums2) == 1:
  _max = nums2[0]
else:
  _max = nums2[-1] + nums2[-2]

if _max >= _sum:
  print("YES")
else:
  print("NO")