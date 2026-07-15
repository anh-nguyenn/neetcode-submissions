class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        curr = []
        res = []
        def dfs(idx, total):
            if total == target:
                res.append(curr[:])
                return 
            if idx == n or total > target:
                return 
            # Decision to go deeper with current idx
            curr.append(nums[idx])
            dfs(idx, total + nums[idx])
        
            # Decision to not choose and increate idx
            curr.pop()
            dfs(idx+1, total)

        dfs(0, 0)

        return res