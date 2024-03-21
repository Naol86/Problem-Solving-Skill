for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    
    product = 1
    for i in range(x):
        product *= nums[i]
    if 2023 / product == 2023//product:
        print('YES')
        lis = [2023 // product]
        for _ in range(1, y):
            lis.append(1)
        print(*lis)
    else:
        print('NO')