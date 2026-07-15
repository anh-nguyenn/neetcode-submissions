class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, btm = 0, len(matrix) - 1
        while top <= btm:
            mid = (top+btm)//2
            if target > matrix[mid][-1]: # target > biggest value of row
                top = mid + 1
            elif target < matrix[mid][0]:
                btm = mid - 1
            else: # target in row
                break
        if not (top <= btm):
            return False
        mid = (top+btm)//2
        l, r =  0, len(matrix[0]) - 1
        while l <= r:
            m = (l+r)//2
            if  target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True
        return False


            
