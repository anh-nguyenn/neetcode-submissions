class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        1 -> 1,2 -> 1,3 -> 1,2,3

        '''
        res = []
        subset = []
        def dfs(idx):
            if idx >= len(nums):
                res.append(subset[:])
                return
            subset.append(nums[idx])
            dfs(idx + 1)

            subset.pop()
            dfs(idx + 1)
        dfs(0)

        return res
            