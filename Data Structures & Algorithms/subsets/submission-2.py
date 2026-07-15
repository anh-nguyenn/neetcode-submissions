class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        n = len(nums)
        def dfs(idx):
            if idx == n:
                res.append(curr[:])
                return
            curr.append(nums[idx]) 
            dfs(idx+1)

            curr.pop()
            dfs(idx+1)

        dfs(0)
        return res