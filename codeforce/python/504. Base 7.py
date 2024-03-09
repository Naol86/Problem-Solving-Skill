class Solution:
    def convertToBase7(self, num: int) -> str:
        digit = 0
        if num == 0:
            return '0'
        ans = []
        if num < 0:
            num = abs(num)
            ans.append('-')
        while 7**digit - 1 < num:
            digit += 1
        print(digit)
        while digit > 0:
            ans.append(str(num//(7**(digit-1))))
            num = num % (7**(digit-1))
            digit -= 1
        print(ans)
        return ''.join(ans)
