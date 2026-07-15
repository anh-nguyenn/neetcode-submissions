class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        0,0 0,1 0,2   0,3 0,4 0,5     0,6 0,7 0,8
        1,0 1,1 1,2    1,3 1,4 1,5    1,6 1,7 1,8
        2,0, 2,1 2,2     2,3, 2,4 2,5
        
        (x,y) => (1, 4)
        range x: 0, 2
        range y: 3, 5
        '''

        def dupRow(row, board):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
            return True
        def dupCol(col, board):
            seen = set()
            for i in range(9):
                if board[i][col] == ".": continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
            return True
        def dupRange(row, col, board):
            xStart = (row//3)*3
            yStart = (col//3)*3
            seen = set()
            for i in range(xStart, xStart + 3):
                for j in range(yStart, yStart + 3):
                    if board[i][j] == ".": continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True
        for i in range(9):
            for j in range(9):
                res = dupRow(i, board) & dupCol(j, board) & dupRange(i, j, board)
                if not res:
                    return False
        return True



        