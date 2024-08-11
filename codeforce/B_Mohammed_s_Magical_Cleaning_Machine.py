for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  
  count = 0
  
  place_holder = 0
  seeker = 1
  
  while place_holder < x - 1:
    if nums[place_holder] == 0:
      place_holder += 1
      if seeker == place_holder:
        seeker += 1
    elif nums[seeker] == 0:
      count += 1
      nums[place_holder] -= 1
      nums[seeker] += 1
      if seeker != x - 1:
        seeker += 1
    elif seeker == x - 1:
      count += nums[place_holder]
      place_holder += 1
    else:
      seeker += 1
  
  print(count)