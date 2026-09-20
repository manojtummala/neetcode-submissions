class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        visited = set()
        arr = defaultdict(list)
        for i, j in edges:
            arr[i].append(j)
            arr[j].append(i)
        q = deque([(0, -1)])
        
        while q:
            node, parent = q.popleft()
            if node in visited:
                return False
            visited.add(node)

            for nei in arr[node]:
                if nei != parent:
                    q.append((nei, node))
                    
        return len(visited) == n