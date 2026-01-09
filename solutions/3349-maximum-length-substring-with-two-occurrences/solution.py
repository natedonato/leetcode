class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = collections.Counter()
        max_length = 0
        l = 0
        r = 0

        while r < len(s):
            char = s[r]
            counts[char] += 1
            while counts[char] > 2:
                counts[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length
