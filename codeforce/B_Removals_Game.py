for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  nums2 = [int(i) for i in input().split()]
  i = 0
  j = x - 1
  while i < j:
    if {nums[i], nums[j]} != {nums2[i], nums2[j]}:
      print("Alice")
      break
    i += 1
    j -= 1
  else:
    print("Bob")