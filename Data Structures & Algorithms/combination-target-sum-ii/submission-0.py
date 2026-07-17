class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        candidates.sort()
        def dfs(idx, total):
            if total == target:
                res.append(curr[:])
                return
            if idx >= len(candidates) or total > target:
                return

            # decision to include i
            curr.append(candidates[idx])

            dfs(idx+1, total+candidates[idx])

            # decision not to include i
            curr.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1, total)
        dfs(0,0)

        return res