class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target or start >= len(candidates):
                return

            path.append(candidates[start])
            dfs(start+1, path, total + candidates[start])
            path.pop()

            while start + 1 < len(candidates) and candidates[start] == candidates[start+1]:
                start += 1
            dfs(start+1, path, total)

        dfs(0, [], 0)

        return res