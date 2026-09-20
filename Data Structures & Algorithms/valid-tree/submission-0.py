class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for i in adj[node]:
                if i == parent:
                    continue
                if not dfs(i, node):
                    return False
            print(visited)
            return True

        if not dfs(0, -1):
            return False
        
        return len(visited) == n