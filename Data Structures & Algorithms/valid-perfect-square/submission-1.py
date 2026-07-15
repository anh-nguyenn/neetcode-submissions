class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = left + (right - left)//2
            val = mid * mid 
            print(val)
            if val == num:
                return True
            if val < num:
                left = mid + 1
            else:
                right = mid - 1
        return False