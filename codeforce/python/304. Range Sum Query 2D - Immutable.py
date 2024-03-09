class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        temp = [[0] * (len(matrix[0])+1) for i in range(len(matrix) + 1)]
        for i in range(1,len(matrix[0]) + 1):
            for j in range(1,len(matrix)+1):
                temp[j][i] = temp[j][i-1] + matrix[j-1][i-1]
        print(temp)
        for i in range(1, len(temp[0])):
            for j in range(1,len(temp)):
                temp[j][i] = temp[j][i] + temp[j-1][i]
        print(temp)
        self.matrix = temp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row1][col1] + self.matrix[row2+1][col2+1] - self.matrix[row2 + 1][col1] - self.matrix[row1][col2 +1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)