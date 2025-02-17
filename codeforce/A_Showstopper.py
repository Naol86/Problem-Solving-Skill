for _ in range(int(input())):
  a = int(input())
  nums1 = [int(i) for i in input().split()]
  nums2 = [int(i) for i in input().split()]
  
  i = a - 2
  while i >= 0:
    if nums1[i] > nums1[-1] and nums1[i] > nums2[-1]:
      print("No")
      break
    elif nums2[i] > nums2[-1] and nums2[i] > nums1[-1]:
      print("No")
      break
    elif nums1[i] > nums1[-1] and nums1[i] <= nums2[-1] and nums2[i] <= nums1[-1]:
      nums1[i], nums2[i] = nums2[i], nums1[i]
    elif nums2[i] > nums2[-1] and nums2[i] <= nums1[-1] and nums1[i] <= nums2[-1]:
      nums1[i], nums2[i] = nums2[i], nums1[i]
    elif nums1[i] <= nums1[-1] and nums2[i] <= nums2[-1]:
      i -= 1
      continue
    else:
      print("No")
      break
    # print(*nums1)
    # print(*nums2)
    # print('-------------------------------')
    # else:
    #   print("No")
    #   break
    i -= 1
  if i < 0:
    print("Yes")