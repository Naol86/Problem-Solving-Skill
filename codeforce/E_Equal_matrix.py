from math import ceil


for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    matrix = []
    for _ in range(x):
        temp = [int(i) for i in input().split()]
        matrix.append(temp)
    ans = 0
    for i in range(x//2):
        for j in range(y//2):
            _sum = matrix[i][j] + matrix[x-i-1][j] + matrix[i][y-j-1] + matrix[x-i-1][y-j-1]
            avr = _sum / 4
            ans += abs(avr - matrix[i][j])
            ans += abs(avr - matrix[x-i-1][j])
            ans += abs(avr - matrix[i][y-j-1])
            ans += abs(avr - matrix[x-i-1][y-j-1])
    if x % 2 != 0:
        for i in range(y//2):
            _sum = matrix[x//2][i] + matrix[x//2][y-j-1]
            avr = _sum / 2
            ans += abs(avr - matrix[x//2][i])
            ans += abs(avr - matrix[x//2][y-i-1])
    if y % 2 != 0:
        for i in range(x//2):
            _sum = matrix[i][y//2] + matrix[x-i-1][y//2]
            avr = _sum / 2
            ans += abs(avr - matrix[i][y//2])
            ans += abs(avr - matrix[x-i-1][y//2])
    print(int(ans))