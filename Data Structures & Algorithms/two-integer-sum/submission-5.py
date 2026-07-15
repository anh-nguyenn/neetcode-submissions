# Hash Map (One Pass)
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        prev = {}
        for i, num in enumerate(nums):
            comple = target - num
            if comple in prev:
                return [prev[comple], i]
            prev[num] = i
        return []
        



# Hash Map (Two Pass)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # Create hashmap storing value + idx:
#         M = {}
#         for i, num in enumerate(nums):
#             M[num] = i
#         for i in range(len(nums)):
#             re = target - nums[i]
#             if re in M and M[re] != i:
#                 return [i, M[re]]
#         return []
        
