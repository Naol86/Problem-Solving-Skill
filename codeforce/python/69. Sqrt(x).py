class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x < 4:
            return 1
        a = 1
        b = x
        mid = (a + b) // 2
        while mid**2 != x:
            if mid**2 > x:
                b = mid
                mid = (a + b) // 2
            else:
                a = mid
                mid = (a + b) // 2
                if mid**2 < x:
                    while mid**2 <= x:
                        mid +=1
                    return mid-1
        return mid
