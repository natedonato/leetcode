class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        max_v = 0
        max_c = 0
        vowels = "aeiou"

        for key, val in c.items():
            if key in vowels:
                max_v = max(max_v, val)
            else:
                max_c = max(max_c, val)

        return max_v + max_c
