x = input()
lis = [int(i) for i in x]
x = int(x)
temp = x
check = True
while check:
    temp +=1
    temp_lis = []
    for i in str(temp):
        if i in temp_lis:
            break
        else:
            temp_lis.append(i)
    if len(temp_lis) == 4:
        print(temp)
        break