class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dctFrequency = {}
        for i, num in enumerate(nums):
            if num not in dctFrequency.keys():
                dctFrequency[num] = 1
                continue
            else:
                return True
        return False