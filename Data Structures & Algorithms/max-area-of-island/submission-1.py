class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        visit = set()
        def dfs(grid, r, c):
            if r < 0 or r >= ROWS or c<0 or c >= COLS or grid[r][c] == 0 or  (r, c) in visit:
                return 0
            dist = 1
            visit.add((r, c))
            for dr, dc in direction:
                dist += dfs(grid, r+dr, c+dc)
            return dist

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(grid, r, c))
        return area