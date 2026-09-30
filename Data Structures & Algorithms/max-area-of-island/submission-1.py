class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        seen = set()
        area = 0
    
        def dfs(r, c):
            # nonlocal area
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1 or (r, c) in seen:
                return 0
            
            seen.add((r, c))
            # area += 1
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    res = max(res, dfs(r, c))
                    # res = max(res, area)
                    # area = 0

        return res
