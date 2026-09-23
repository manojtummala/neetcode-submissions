class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        arr = []

        for i, h in enumerate(heights):
            start = i
            while arr and arr[-1][1] > h:
                index, height = arr.pop()
                res = max(res, height*(i-index))
                start = index
            arr.append((start, h))

        for i, h in arr:
            res = max(res, h * (len(heights) - i))
        return res