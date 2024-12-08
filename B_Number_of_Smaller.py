x, y = map(int, input().split())

nums1 = [int(i) for i in input().split()]
nums2 = [int(i) for i in input().split()]

nums1.append(float('inf'))
ans = []

j = 0 # points nums1
i = 0 # points nums2

while i < y:
  while nums2[i] > nums1[j]:
    j += 1
  ans.append(j)
  i += 1
print(*ans)

