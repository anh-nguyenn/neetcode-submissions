class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
        dist = 0
        def addNum(r, c):
            if r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visit or grid[r][c] == -1:
                return
            q.append((r,c))
            visit.add((r,c))
        while q:
            interval = len(q)
            for k in range(interval):
                r, c = q.popleft()
                grid[r][c] = dist
                addNum(r+1, c)
                addNum(r-1, c)
                addNum(r, c+1)
                addNum(r, c-1)
            dist += 1
        
