class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        arr = []
        res = 0

        left, right = [-1]*n, [n]*n
        for i in range(n):
            while arr and heights[arr[-1]] >= heights[i]:
                arr.pop()
            if arr:
                left[i] = arr[-1]
            arr.append(i)

        arr = []
        for i in range(n-1, -1, -1):
            while arr and heights[arr[-1]] >= heights[i]:
                arr.pop()
            if arr:
                right[i] = arr[-1]
            arr.append(i)

        for i in range(n):
            left[i] += 1
            right[i] -= 1
            res = max(res, heights[i] * (right[i] - left[i] + 1))

        return res