class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                a, b = dr + r, dc + c
                if 0<=a<rows and 0<=b<cols and grid[a][b] == INF:
                    grid[a][b] = grid[r][c] + 1
                    queue.append((a, b))