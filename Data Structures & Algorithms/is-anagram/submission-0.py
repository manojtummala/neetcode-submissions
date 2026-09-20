class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}

        for ch in s:
            h[ch] = h.get(ch, 0) + 1
        
        for ch in t:
            if ch not in h or h[ch] == 0:
                return False
            h[ch] -= 1

        
        for key, val in h.items():
            if val != 0:
                return False
        return True