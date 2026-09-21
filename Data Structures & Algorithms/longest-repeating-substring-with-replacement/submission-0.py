class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        ma = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1

            ma = max(ma, count[s[i]])

            while i - l + 1 - ma > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, i - l + 1)

        return res
