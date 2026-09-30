class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        seen = set()
        area = 0
    
        def dfs(r, c):
            nonlocal area
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1 or (r, c) in seen:
                return
            
            seen.add((r, c))
            area += 1
            for dr, dc in directions:
                dfs(dr+r, dc+c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    dfs(r, c)
                    res = max(res, area)
                    area = 0

        return res
