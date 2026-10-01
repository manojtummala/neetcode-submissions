class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        inf = 2147483647
        seen = set()

        q = deque()

        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in seen or grid[r][c] == -1:
                return
            seen.add((r, c))
            q.append([r, c])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))

        res = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = res
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    dfs(nr, nc)

            res += 1