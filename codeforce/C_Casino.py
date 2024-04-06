x = int(input())

def prime_fac(n: int):
    pro = 1
    i = 2
    while i * i <= n:
        while n % i == 0:
            if i not in {2,3}:
                pro *= i
            n //= i
        i += 1
    if n not in {2,3}:x
        pro *= n
    return pro

nums = [int(i) for i in input().split()]

pro = prime_fac(nums[0])
# print(pro)

for num in nums[1:]:
    if num % pro != 0:
        print("No")
        break
    temp = prime_fac(num // pro)
    # print(temp,'this is temp')
    if temp != 1:
        print("No")
        break
else:
    print("Yes")