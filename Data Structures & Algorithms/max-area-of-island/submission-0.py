class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        direction = [[1, 0], [-1, 0],[0, 1], [0,-1]]
        
        def dfs(grid, r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            dist = 1
            for dr, dc in direction:
                dist += dfs(grid, r + dr, c + dc)
            return dist

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(dfs(grid, r, c), res)
        
        return res
                    


        