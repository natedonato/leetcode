class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) > 1:
            y = -heapq.heappop(h)
            x = -heapq.heappop(h)
            if x != y:
                heapq.heappush(h, -(y - x))

        if h:
            return -h[0]
        else:
            return 0
