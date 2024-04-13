x = int(input())
nums = [int(i) for i in input().split()]

arr = [0,0,0]
for i in range(x):
  arr[i%3] += nums[i]
# print(arr)
if arr[0] > arr[1] and arr[0] > arr[2]:
  print("chest")
elif arr[1] > arr[0] and arr[1] > arr[2]:
  print("biceps")
else:
  print("back")