
for _ in range(int(input())):
  x = int(input())
  nums1 = [int(i) for i in input().split()]
  nums2 = [int(i) for i in input().split()]
  for i in range(x):
    if nums1[i] > nums2[i]:
      temp = nums1[i]
      nums1[i] = nums2[i]
      nums2[i] = temp
    # else:
    #   temp = nums2[i]
    #   nums2[i] = nums1[i]
    #   nums1[i] = temp
  # print(nums1)
  # print(nums2)
  print(max(nums1) * max(nums2))