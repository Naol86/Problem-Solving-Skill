import numpy as np
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = np.zeros(len(s),dtype="int32")
        for i in shifts:
            if i[-1] == 0:
                temp[i[0]:i[1]+1] = temp[i[0]:i[1]+1] - 1
            else:
                temp[i[0]:i[1]+1] = temp[i[0]:i[1]+1] + 1
        ans = ""
        a = ord('a')
        z = ord('z')
        for i in range(len(s)):
            ch = ord(s[i]) + temp[i]
            if ch >= a and ch <= z:
                ans += chr(ch)
            elif ch > z:
                ch = (ch - z)%26 + a - 1
                if ch < a:
                    ch = z - (a - ch )%26 + 1
                ans += chr(ch)
            elif ch < a:
                ch = z - (a - ch )%26 + 1  
                if ch > 122:
                    ch = (ch - z)%26 + a - 1
                ans += chr(ch)
        return ans