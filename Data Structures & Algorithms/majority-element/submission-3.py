# Another hashmap => take count of the biggest freq in the array
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, maxCount = 0, 0
        M = {}
        for num in nums:
            M[num] = 1 + M.get(num, 0)
            if maxCount < M[num]:
                maxCount = M[num]
                res = num
        return res


# Sorting with linear time and O(1) space
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         mid = len(nums)//2
#         nums.sort()
#         return nums[mid]


# brute force
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         mid = len(nums)//2
#         for num in nums:
#             count = sum(1 for i in nums if  i == num)
#             if count > mid:
#                 return num
