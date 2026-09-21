class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        h = {']': '[', '}' : '{', ')': '('}

        for ch in s:
            if ch in h:
                if arr and arr[-1] == h[ch]:
                    arr.pop()
                else:
                    return False
            else:
                arr.append(ch)
        
        return True if not arr else False