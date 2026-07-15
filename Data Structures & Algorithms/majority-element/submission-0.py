class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        M = {}
        ele_len = len(nums)//2
        for num in nums:
            M[num] = 1 + M.get(num, 0)
        for k, v in M.items():
            if v > ele_len:
                return k