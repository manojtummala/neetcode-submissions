class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()
        c = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for i in adj[node]:
                dfs(i)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                c += 1
        return c
                