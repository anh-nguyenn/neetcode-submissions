class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        k = 1 # longest consecutive
        maxK = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                k += 1
                continue
            else:
                maxK = max(k, maxK)
                k = 1
        return max(k, maxK)

