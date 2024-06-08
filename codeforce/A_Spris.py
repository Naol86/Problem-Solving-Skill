a = int(input())
b = int(input())
c = int(input())
count = 0
while a > 0 and b > 1 and c > 3:
  count += 7
  a -= 1
  b -= 2
  c -= 4
print(count)