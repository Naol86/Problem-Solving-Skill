n = int(input())
boys = [int(i) for i in input().split()]
m = int(input())
girls = [int(i) for i in input().split()]
boys.sort()
girls.sort()

i = 0
j = 0
count = 0
while i < n and j < m:
  if abs(boys[i] - girls[j]) <= 1:
    count += 1
    i += 1
    j += 1
  elif boys[i] > girls[j]:
    j += 1
  elif boys[i] < girls[j]:
    i += 1
print(count)