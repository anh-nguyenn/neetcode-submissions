class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        if nums[-1] < target:
            return len(nums)
        while i < len(nums):
            if nums[i] == target or nums[i] > target:
                return i
            i += 1
