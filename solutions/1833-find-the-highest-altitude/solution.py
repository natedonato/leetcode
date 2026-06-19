class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        alt = 0

        for d in gain:
            alt += d
            m = max(m, alt)

        return m
