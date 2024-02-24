x = int(input())
lis = [int(i) for i in input().split()]
lis.sort()
people = 0
time = 0
for i in lis:
    if time <= i:
        people += 1
        time += i
print(people)