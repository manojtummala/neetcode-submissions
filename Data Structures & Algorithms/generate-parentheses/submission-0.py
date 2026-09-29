class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s):
            op = 0
            for c in s:
                op += 1 if c == '(' else -1
                if op < 0:
                    return False
            return not op

        def dfs(s):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')

        dfs('')

        return res