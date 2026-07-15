class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        shortest = float('inf')

        for i in range(n):
            tmp = 0
            for j in range(i, n):
                tmp += nums[j]
                if tmp >= target:
                    shortest = min(j+1-i, shortest)
                    break
        return 0 if shortest == float('inf') else shortest

