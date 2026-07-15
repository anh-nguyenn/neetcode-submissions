#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums)//2
        nums.sort()
        return nums[mid]


# brute force
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         mid = len(nums)//2
#         for num in nums:
#             count = sum(1 for i in nums if  i == num)
#             if count > mid:
#                 return num
