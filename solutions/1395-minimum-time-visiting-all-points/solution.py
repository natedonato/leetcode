class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0

        c = points[0]
        for p in points:
            dist = max(abs(p[0] - c[0]), abs(p[1] - c[1]))
            total += dist
            c = p

        return total
