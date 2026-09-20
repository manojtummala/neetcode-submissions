class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = [ch for ch in s if ch.isalnum()]
        l, r = 0, len(arr)-1

        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True