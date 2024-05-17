a, b = map(int, input().split())


_max = max(a, b)
ans = _max
diff = abs(a - b)

if diff < 2:
  print(a ^ b)

else:
  leng = diff.bit_length()
  print(leng, 1<<(leng - 1))