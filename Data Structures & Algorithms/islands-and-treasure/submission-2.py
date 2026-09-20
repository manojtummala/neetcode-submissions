class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 0
        
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque()
        inf = 2147483647
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            i, j = q.popleft()
            for dr, dc in direction:
                ni, nj = dr + i, dc + j
                if ni in range(rows) and nj in range(cols) and grid[ni][nj] == inf:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni, nj))

