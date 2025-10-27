class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = [ [p[0]**2 + p[1]** 2, [p[0], p[1]]] for p in points]

        heapq.heapify(d)

        out = []
        for _ in range(k):
            out.append(heapq.heappop(d)[1])

        return out
