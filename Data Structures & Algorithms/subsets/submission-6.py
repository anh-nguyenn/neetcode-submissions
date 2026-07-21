class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):
            if i == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)
        
        dfs(0)

        return res
    
    """
                []
       [1]                      []
    [1,2][1]                [2] [0] 
[1,2,3] [1,2] [1,3]  [1]    [2]

dfs(0) -> curr=[1]
        -> dfs(1) -> curr=[1,2]
            ->dfs(2) -> curr= [1,2,3]
            -> dfs(2) -> curr[1,2]
        -> dfs(1) -> curr = [1]
            -> dfs(2) -> curr = [1,3]
            -> dfs(2) -> curr = [1]
dfs(0) -> curr = []
        -> dfs(1)
    """