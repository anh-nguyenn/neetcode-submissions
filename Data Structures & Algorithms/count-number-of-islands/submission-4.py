from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        visit = set()
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc
                    new_loc = (new_row), (new_col)
                    if (0 <= new_row < ROWS and 0 <= new_col < COLS and 
                    grid[new_row][new_col] == "1" and new_loc not in visit):
                        queue.append(new_loc)
                        visit.add(new_loc)
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    res += 1 
                    bfs(r, c)
        return res