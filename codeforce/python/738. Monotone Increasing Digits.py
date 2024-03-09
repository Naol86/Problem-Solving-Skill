import numpy as np
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if len(str(n)) < 2:
            return n
        lis = [i for i in str(n)]
        lis = np.array(lis)
        for i in range(len(lis)-1):
            if lis[i] > lis[i+1]:
                lis[i] = str(int(lis[i])-1)
                lis[i+1:] = '9'
                lis = ''.join(lis)
                ans = int(lis)
                return self.monotoneIncreasingDigits(ans)
        return n
