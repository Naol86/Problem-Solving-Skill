import math

MOD = 1000000007
for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    
    _sum = 0
    _max = 0 
    prev = 0
    for i in nums:
        _sum += i
        if prev + i > 0:
            prev += i
            _max = max(_max, prev)
        else:
            prev = 0
    temp = int(2 ** y) - 1
    
    print((_sum + (temp * _max)) % MOD)
    
    
    


def palindrome(s):
    return s == s[::-1]