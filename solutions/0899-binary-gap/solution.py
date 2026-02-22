class Solution:
    def binaryGap(self, n: int) -> int:
        best = 0
        dist = 0
        for c in bin(n)[3:]:
            dist += 1
            if c == "1":
                best = max(best, dist)
                dist = 0

        return best
