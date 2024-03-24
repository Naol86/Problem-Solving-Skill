n, m, a = [int(i) for i in input().split()]

left = n // a + 1

down = m // a + 1

# print(left, down)
if m % a == 0:
    down -= 1
if n % a == 0:
    left -= 1
print(left * down)