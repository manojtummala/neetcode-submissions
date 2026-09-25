class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x == y:
                continue
            else:
                heapq.heappush(heap, -((-x) + y))
        return -heap[0] if heap else 0