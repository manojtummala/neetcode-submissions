class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        
        res = []
        window = {}
        for i in range(len(nums)):
            curr = nums[i]
            window[curr] = window.get(curr, 0) + 1
            if i - l + 1 > k:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1
            if i - l + 1 == k:
                ma = max(window.keys())
                res.append(ma)
        return res