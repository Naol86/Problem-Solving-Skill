x = input()
lis = []
for i in x:
    if i not in lis:
        lis.append(i)
if len(lis)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")