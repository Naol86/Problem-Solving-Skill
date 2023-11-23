x = input()
dic = {}
f = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
lis = f.split()
Find = []
for i in lis:
    dic[i] = 0
if len(x) < 26:
    print(-1)
else:
    temp = dic.copy()
    temp_lis = lis.copy()
    co = 0
    for i in x:
        if i not in lis:
            Find.append(co)
        elif temp[i] != 1:
            temp[i] = 1
            temp_lis.remove(i)
        else:
            temp = dic.copy()
            temp_lis = lis.copy()
            temp[i] = 1
            temp_lis.remove(i)
            Find = []
        co+=1
    if len(temp_lis) > len(Find):
        print(-1)
    else:
        temp = [i for i in x]
        for j in range(len(Find)):
            if len(temp_lis) > j:
                temp[Find[j]] = temp_lis[j]
            else:
                temp[Find[j]] = "A"
        print("".join(temp))