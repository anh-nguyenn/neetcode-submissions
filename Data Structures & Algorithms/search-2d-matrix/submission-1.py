class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c = len(matrix[0]) - 1
        r = 0
        while r < len(matrix) and c >= 0:
            pivot = matrix[r][c]
            print(pivot)
            if pivot == target:
                return True
            elif pivot > target:
                c -= 1
            else:
                r += 1  
        return False