class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        q = deque()
        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            while q:
                r, c = q.popleft()
                for dr, dc in direction:
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < ROWS and 0 <= cc < COLS and grid[rr][cc] == "1" and (rr, cc) not in visit:
                        visit.add((rr, cc))
                        q.append((rr,cc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1"  and (r,c) not in visit:
                    res += 1
                    bfs(r, c)
                    
        return res
        