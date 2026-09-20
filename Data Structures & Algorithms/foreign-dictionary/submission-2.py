class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        order = defaultdict(set)
        indegree = {c:0 for w in words for c in w}
        n = len(words)

        i = 0

        while (i + 1) < n:
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i].startswith(words[i+1]) and len(words[i]) > len(words[i+1]):
                    return ''
                if words[i][j] != words[i+1][j]:
                    if words[i+1][j] not in order[words[i][j]]:
                        order[words[i][j]].add(words[i+1][j])
                        indegree[words[i+1][j]] += 1
                    break
            i += 1

        q = deque([c for c in indegree if indegree[c]==0])
        res = []

        while q:
            curr = q.popleft()
            print(curr)
            res.append(curr)

            for nei in order[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) < len(indegree):
            return ""
        
        return ''.join(res)