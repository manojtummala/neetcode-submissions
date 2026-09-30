class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        res = 0
        seen = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in seen or grid[r][c] != '1':
                return
            
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    dfs(r, c)
                    res += 1

        return res