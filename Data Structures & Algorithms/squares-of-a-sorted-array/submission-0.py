class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for item in nums:
            res.append(item*item)
        return sorted(res)