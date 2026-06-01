class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        c = collections.Counter(str(n))

        s = 0
        for item in c:
            s += int(item) * c[item]
        return s
