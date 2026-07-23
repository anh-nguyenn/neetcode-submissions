class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        def dfs(r,c):
            visit.add((r,c))
            for dr, dc in direction:
                if 0<=r+dr<ROWS and 0<=c+dc<COLS and grid[r+dr][c+dc] == "1" and ((r+dr, c+dc) not in visit):
                    dfs(r+dr, c+dc)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1"  and (r,c) not in visit:
                    res += 1
                    dfs(r, c)
                    
        return res
        