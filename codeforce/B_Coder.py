x = int(input())

a = ['C.'] * (x//2) + ['C'] * (x%2)
b = ['.C'] * (x//2) + ['.'] * (x%2)

num1 = (x//2) + (x%2)
num2 = x - num1

sums = (num1 * (x//2) + num1 * (x%2)) + (num2 * (x//2))

print(sums)
for i in range(x):
  if i % 2 == 0:
    print(''.join(a))
  else:
    print(''.join(b))