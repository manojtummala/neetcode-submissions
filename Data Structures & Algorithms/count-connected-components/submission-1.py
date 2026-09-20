class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        arr = defaultdict(list)

        for a, b in edges:
            arr[a].append(b)
            arr[b].append(a)

        res = 0
        visited = set()

        def dfs(node):
            for nei in arr[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res+=1
                
        return res



            