x = int(input())
lis = [i for i in input()]

i = 2
while i < x + 1:
    if x % i == 0:
        lis = lis[:i][::-1] + lis[i:]
    i += 1
    
print(''.join(lis))

