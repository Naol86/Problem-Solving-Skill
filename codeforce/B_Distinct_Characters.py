import sys 
input = sys.stdin.readline

s = input()
lis = [i for i in s]
lis.append('A')
for i in range(1, len(lis) - 1):
    if lis[i - 1] == lis[i]:
        temp = ord('a')
        while temp == ord(lis[i - 1]) or temp == ord(lis[i + 1]):
            temp += 1
        lis[i] = chr(temp)
print(''.join(lis[:-1]))