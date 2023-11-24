x = int(input())
while True:
    x +=1
    temp_dic = {}
    for i in str(x):
        if i in temp_dic:
            break
        else:
            temp_dic[i] = 0
    if len(temp_dic) == 4:
        print(x)
        break
