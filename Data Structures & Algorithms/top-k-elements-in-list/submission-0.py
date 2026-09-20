class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        arr = []

        for num in count.keys():
            heapq.heappush(arr, [count[num], num])
            if len(arr) > k:
                heapq.heappop(arr)

        res = []
        for i in range(k):
            res.append(heapq.heappop(arr)[1])
        return res