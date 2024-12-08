n, k = map(int, input().split())
temp = 1 if n % 2 else 0

odd = n // 2 + temp
even = n - odd

# print(odd, even)

if k > odd:
  k -= odd
  print(k * 2)
else:
  print(k * 2 - 1)