class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = Counter(s)
        even_freq = math.inf
        odd_freq = 0

        for i in freqs.values():
            if i % 2 == 0:
                even_freq = min(even_freq, i)
            else:
                odd_freq = max(odd_freq, i)

        return odd_freq - even_freq
