class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        arr = []

        def dfs(op, cl):
            if op == cl == n:
                res.append(''.join(arr))
                return
            
            if op < n:
                arr.append('(')
                dfs(op + 1, cl)
                arr.pop()
            
            if cl < op:
                arr.append(')')
                dfs(op, cl + 1)
                arr.pop()
        dfs(0, 0)
        return res