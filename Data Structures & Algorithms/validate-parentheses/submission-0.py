class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')

        return s == ''
        
        
        
        # arr = []

        # h = {'[': ']', '{' : '}', '(': ')'}

        # for ch in s:
        #     if ch == ']':
        #         if arr[-1] != '[':
        #             return False
        #     elif ch == '}':
        #         if arr[-1] != '{':
        #             return False
        #     elif ch == ')':
        #         if arr[-1] != '(':
        #             return False
        #     else:
        #         arr.append(ch)
        
        # return True