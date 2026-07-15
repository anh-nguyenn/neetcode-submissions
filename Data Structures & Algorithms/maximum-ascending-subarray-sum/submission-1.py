class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        biggest = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                biggest += nums[i]
            else:
                biggest = nums[i]
            res = max(biggest, res)
        return res

            