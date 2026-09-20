class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        visited = set()
        arr = defaultdict(list)
        for i, j in edges:
            arr[i].append(j)
            arr[j].append(i)

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in arr[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n