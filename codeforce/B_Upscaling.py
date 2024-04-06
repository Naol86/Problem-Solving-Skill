a = {0:'##', 1:'..'}

for _ in range(int(input())):
    x = int(input())
    for i in range(x):
        for j in range(2):
            lis = []
            for k in range(x):
                lis.append(a[(i + k)%2])
            print(''.join(lis))
