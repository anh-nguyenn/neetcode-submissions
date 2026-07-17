class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(idx, total):
            if total == target:
                res.append(curr[:])
                return
            if idx == len(nums) or total > target:
                return
            
            # decicion to include nums[i]
            curr.append(nums[idx])
            dfs(idx, total+nums[idx])
            # decision to skip nums[i]
            curr.pop()
            dfs(idx + 1, total)
        
        dfs(0, 0)

        return res