class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        num = x
        if n > 0:
            while n > (2**31 -1):
                num = num ** (2**31 -1)
                n -= (2**31 -1)
            if n != 0:
                num = num ** n
        elif n < 0:
            while n < -(2**31 + 1):
                num = num**(-(2**31+1))
                n += (2**31+1)
            if n!=0:
                num = num ** n
        return num
