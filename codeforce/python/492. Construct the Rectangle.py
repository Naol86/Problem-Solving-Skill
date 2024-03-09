class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area < 4:
            return [area, 1]
        for i in range(int(math.sqrt(area + 1)),1,-1):
            if area%i == 0:
                return [area//i , i]
        else:
            return [area, 1]
