class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h

        l = 1
        r = max(piles)

        while l < r:
            mid = (r - l) // 2 + l
            if self.canFinish(mid):
                r = mid
            else:
                l = mid + 1

        return l

    def canFinish(self, k):
        count = 0
        for p in self.piles:
            count += math.ceil(p / k)
        return count <= self.h
