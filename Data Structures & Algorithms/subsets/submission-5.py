class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            
            # decision to include nums[i]
            curr.append(nums[i])
            dfs(i+1)
            # decision to NOT include nums[i]

            curr.pop()
            dfs(i+1)
        dfs(0)
        return res