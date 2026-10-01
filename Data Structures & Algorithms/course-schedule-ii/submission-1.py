class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)


        res = []
        seen, cycle = set(), set()

        def dfs(c):
            if c in cycle:
                return False
            if c in seen:
                return True
            
            cycle.add(c)
            for pre in prereq[c]:
                if dfs(pre) == False:
                    return False
            cycle.remove(c)
            seen.add(c)
            res.append(c)

            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res