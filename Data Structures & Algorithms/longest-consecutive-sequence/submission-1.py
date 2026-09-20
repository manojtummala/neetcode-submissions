class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = defaultdict(int)
        res = 0

        for num in nums:
            if not h[num]:
                h[num] = h[num-1] + h[num+1] + 1
                h[num - h[num-1]] = h[num]
                h[num + h[num+1]] = h[num]
                res = max(res, h[num])
        return res