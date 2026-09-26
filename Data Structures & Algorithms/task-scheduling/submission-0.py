class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        arr = [-c for c in count.values()]
        heapq.heapify(arr)

        t = 0
        q = deque()
        while arr or q:
            t += 1
            if not arr:
                t = q[0][1]
            else:
                c = 1 + heapq.heappop(arr)
                if c:
                    q.append([c, t + n])
            if q and q[0][1] == t:
                heapq.heappush(arr, q.popleft()[0])

        return t