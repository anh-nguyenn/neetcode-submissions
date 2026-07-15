class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, shortest = 0, float('inf')

        for r in range(len(nums)):
            total = sum(nums[l:r+1])
            while total >= target:
                shortest = min(r - l + 1, shortest)
                total -= nums[l]
                l += 1
        
        return 0 if shortest == float('inf') else shortest

        
            