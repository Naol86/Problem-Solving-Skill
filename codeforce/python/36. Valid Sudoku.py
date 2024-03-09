class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        sub_box = [[set([]) for i in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                temp_num = board[i][j]
                if temp_num == '.':
                    continue
                if temp_num in row[i]:
                    return False
                else:
                    row[i].add(temp_num)
                if temp_num in col[j]:
                    return False
                else:
                    col[j].add(temp_num)
                sub_box_i = i//3
                sub_box_j = j//3
                if temp_num in sub_box[sub_box_i][sub_box_j]:
                    return False
                else:
                    sub_box[sub_box_i][sub_box_j].add(temp_num)
        return True
