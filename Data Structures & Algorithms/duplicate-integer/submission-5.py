# Using sort
# Time: O(nlogn)
# Space: O(1)
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort() # nlogn
#         for i in range(1, len(nums)): #n
#             if nums[i] == nums[i-1]:
#                 return True
#         return False

# Using set
# class Solution:
#     def hasDuplicate(self, nums):
#         return (len(set(nums)) < len(nums))


class Solution:
    def hasDuplicate(self,nums):
        seen = set()
        for ele in nums:
            if ele in seen:
                return True
            seen.add(ele)
        return False
        