import sys

input = sys.stdin.readline

x = input()
# print(x, len(x))
leng = len(x) - 1
dec = []
for i in range(leng):
    if x[i] == '4':
        dec.append('0')
    else:
        dec.append('1')
temp = 0
temp = int('1' * leng, 2)
# print(temp, dec)
temp += int(''.join(dec), 2)

print(temp)