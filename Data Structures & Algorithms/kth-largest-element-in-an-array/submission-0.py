class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-i for i in nums]

        heapq.heapify(arr)
        res = float('-inf')

        while k > 0:
            res = -(heapq.heappop(arr))
            k -= 1

        return res