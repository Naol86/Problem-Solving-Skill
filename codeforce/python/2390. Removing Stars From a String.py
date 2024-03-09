class Solution:
    def removeStars(self, s: str) -> str:
        lis = []
        for i in s:
            if i != "*":
                lis.append(i)
            else:
                lis.pop()
        return ''.join(lis)
