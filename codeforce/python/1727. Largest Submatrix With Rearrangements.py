import numpy as np
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        for i in range(len(matrix)):
            matrix[i].sort(reverse=True)
        _max = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = matrix[i][j] * (j + 1)
                if temp > _max:
                    _max = temp
        print(matrix)
        return _max