for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  odd = []
  even = []
  for num in nums:
    if num %2:
      odd.append(num)
    else:
      even.append(num)
  odd.sort()
  even.sort()
  
  # print(even, odd)
  
  alice = 0
  bob = 0
  
  turn = True
  
  while odd or even:
    if even and odd:
      if turn:
        if even[-1] > odd[-1]:
          alice += even.pop()
        else:
          odd.pop()
      else:
        if even[-1] < odd[-1]:
          bob += odd.pop()
        else:
          even.pop()
    else:
      if even:
        if turn:
          alice += even.pop()
        else:
          even.pop()
      else:
        if turn:
          odd.pop()
        else:
          bob += odd.pop()
    turn = not turn
    # print(even, odd)
  # print(alice, bob)
  if alice > bob:
    print("Alice")
  elif bob > alice:
    print("Bob")
  else:
    print("Tie")