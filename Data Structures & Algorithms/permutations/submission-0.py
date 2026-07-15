class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]
        
        subset = self.permute(nums[1:])
        res = []
        for s in subset:
            for i in range(len(s) + 1):
                s_copy = s[:]
                s_copy.insert(i, nums[0])
                res.append(s_copy)
        return res

