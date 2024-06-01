notes = [1, 5, 10, 20, 100]
x = int(input())

count = 0
if x >= 100:
  count += (x//100)
  x %= 100
if x >= 20:
  count += (x//20)
  x %= 20
if x >= 10:
  count += (x//10)
  x %= 10
if x >= 5:
  count += (x//5)
  x %= 5
if x >= 1:
  count += (x//1)
  x %= 1
print(count)