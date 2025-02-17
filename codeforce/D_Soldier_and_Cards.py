from collections import deque


n = int(input())
nums1 = [int(i) for i in input().split()]
nums2 = [int(i) for i in input().split()]
len1 = nums1[0]
len2 = nums2[0]
nums1 = deque(nums1[1:])
nums2 = deque(nums2[1:])

count = 0
while count < n * 6000:
  x = nums1.popleft()
  y = nums2.popleft()
  len1 -= 1
  len2 -= 1
  
  
  if x > y:
    nums1.append(y)
    nums1.append(x)
    len1 += 2
  else:
    len2 += 2
    nums2.append(x)
    nums2.append(y)
  # print(nums1)
  # print(nums2)
  
  count += 1
  if len1 == 0:
    print(count, 2)
    break
  if len2 == 0:
    print(count, 1)
    break
else:
  print(-1)