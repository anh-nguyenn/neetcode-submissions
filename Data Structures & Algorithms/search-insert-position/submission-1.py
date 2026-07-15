class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return at the index nearly == target
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if target < nums[mid]: #target on the left
                right = mid - 1
            else:
                left = mid + 1
        return left