class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.M = {}
        self.matrix = matrix
        for i in range(len(matrix)):
            self.M[i] = matrix[i]
        print(self.M)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        while row1 <= row2:
            tmp = row1
            for i in range(col1, col2+1):
                res += self.matrix[tmp][i]
            row1 += 1
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
'''
[
0: [3, 0, 1, 4, 2], 
1: [5, 6, 3, 2, 1], 
2: [1, 2, 0, 1, 5], 
3: [4, 1, 0, 1, 7], 
4: [1, 0, 3, 0, 5]]
'''