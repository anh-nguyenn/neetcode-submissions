class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        directions = [(1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)]

        queue = deque()
        queue.append((0, 0, 1))  # (row, col, distance)
        visited = {(0, 0)}

        while queue:
            r, c, dist = queue.popleft()

            if r == ROWS - 1 and c == COLS - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == 0 and
                    (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

        return -1  # no path found