class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direction = [[1,0], [-1, 0], [0, 1], [0,-1]]
        
        def dfs(grid, r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return
            grid[r][c] = 0
            print(grid)
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                print(nr, nc)
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS:
                    continue
                if grid[nr][nc] == "1":
                    dfs(grid, nr, nc)
            

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                # print(i, j, grid[i][j])
                if grid[i][j] == "1":
                    # print(i, j)
                    dfs(grid, i, j)
                    res += 1
        
        return res

