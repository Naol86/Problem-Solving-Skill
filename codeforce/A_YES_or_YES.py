for i in range(int(input())):
    x = input()
    one = set(["y","Y"])
    two = set(["E","e"])
    three = set(["S","s"])
    dic = {0:one , 1: two, 2:three}
    for j in range(3):
        if x[j] not in dic[j]:
            print("NO")
            break
    else:
        print("YES")
