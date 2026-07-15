import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left+right)//2
            total = 0
            for num in piles:
                total += math.ceil(num/mid)
            if total <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res