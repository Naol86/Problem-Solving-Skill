class Solution:
    def knightDialer(self, n: int) -> int:
        lis = [1] * 10
        for i in range(2,n+1):
            old_lis = lis.copy()
            lis[0] = old_lis[4] + old_lis[6]
            lis[1] = old_lis[8] + old_lis[6]
            lis[2] = old_lis[7] + old_lis[9]
            lis[3] = old_lis[4] + old_lis[8]
            lis[4] = old_lis[3] + old_lis[9] + old_lis[0]
            lis[5] = 0
            lis[6] = old_lis[1] + old_lis[7] + old_lis[0]
            lis[7] = old_lis[2] + old_lis[6]
            lis[8] = old_lis[1] + old_lis[3]
            lis[9] = old_lis[2] + old_lis[4]
        return sum(lis) % ((10 **9) + 7)
