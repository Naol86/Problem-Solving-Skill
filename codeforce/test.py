from functools import lru_cache

@lru_cache(maxsize=3)
def fibo(a):
  if a < 2:
    return a
  return fibo(a - 1) + fibo(a-2)

print(fibo(100))