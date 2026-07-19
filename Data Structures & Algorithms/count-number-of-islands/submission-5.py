class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direction = [[1,0], [-1, 0], [0, -1], [0, 1]]

        res = 0
        visit = set()
        def dfs(grid, r, c):
            if r <0 or r >= ROWS or c <0 or c >= COLS or grid[r][c] == "0" or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in direction:
                new_row = r + dr
                new_col = c + dc
                dfs(grid, new_row, new_col)
                
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    res += 1
                    dfs(grid, r, c)
        return res