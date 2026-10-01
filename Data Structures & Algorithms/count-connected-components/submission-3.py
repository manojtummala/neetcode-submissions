class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        seen = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            seen[node] = True
            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if not seen[nei]:
                        q.append(nei)
                        seen[nei] = True
        
        res = 0

        for node in range(n):
            if not seen[node]:
                bfs(node)
                res += 1

        return res