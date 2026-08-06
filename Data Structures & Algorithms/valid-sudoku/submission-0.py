class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.validRow(row):
                return False
        if not self.validColumns(board):
            return False

        if not self.validSubBoxes(board):
            return False
            
        return True
        

    def validRow(self, row):
        hashRow = {}
        for key in row:
            if key == '.':
                continue
            if key in hashRow:
                return False
            else:
                hashRow[key] = 1
        return True

    def validColumns(self, board):
        for col in zip(*board): 
            if not self.validRow(col):
                return False
        return True


    def validSubBoxes(self, board):
        for i in range(3):
            for j in range(3):
                box = [board[r][c]
                    for r in range(3*i, 3*i + 3)
                    for c in range(3*j, 3*j + 3)]
                if not self.validRow(box):
                    return False
        return True

        
        

        