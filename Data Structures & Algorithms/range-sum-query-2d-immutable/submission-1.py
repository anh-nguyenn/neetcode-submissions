'''
Prefix sum:
[0, 0, 0, 0, 0, 0]
[0, 3, 0, 1, 4, 2], 
[0, 5, 6, 3, 2, 1], 
[0, 1, 2, 0, 1, 5], 
[0, 4, 1, 0, 1, 7], 
[0, 1, 0, 3, 0, 5]]
'''
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.prefixSum = [[0]*(col +1) for _ in range(row + 1)]
        for r in range(row):
            prefix = 0
            for c in range(col): # loop through matrix
                prefix += matrix[r][c]
                above = self.prefixSum[r][c+1]
                self.prefixSum[r+1][c+1] = prefix + above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefixSum[row2+1][col2+1]
        right = self.prefixSum[row1][col2+1]
        left = self.prefixSum[row2+1][col1]
        topleft = self.prefixSum[row1][col1]

        return bottomRight - right - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)