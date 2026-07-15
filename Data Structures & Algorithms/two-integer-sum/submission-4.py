class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create hashmap storing value + idx:
        M = {}
        for i, num in enumerate(nums):
            M[num] = i
        for i in range(len(nums)):
            re = target - nums[i]
            if re in M and M[re] != i:
                return [i, M[re]]
        return []
        
