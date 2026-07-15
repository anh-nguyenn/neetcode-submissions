class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            # decision to include nums[i]
            path.append(nums[i])
            dfs(i+1,path)
            # decision not to include nums[i]
            path.pop()
            dfs(i+1, path)
        
        dfs(0, [])

        return res