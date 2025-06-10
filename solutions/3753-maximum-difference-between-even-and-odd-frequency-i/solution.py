class Solution:
    def maxDifference(self, s: str) -> int:
        counts = collections.Counter(s)
        odd = -math.inf
        even = math.inf

        for count in counts.values():
            if count % 2 == 0:
                even = min(even, count)
            else:
                odd = max(odd, count)

        return odd - even

