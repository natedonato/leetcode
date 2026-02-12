class Solution:
    def longestBalanced(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            c = collections.Counter()
            max_count = 0
            for j in range(i, len(s)):
                char = s[j]
                c[char] += 1
                max_count = max(max_count, c[char])

                if all([count == max_count for count in c.values()]):
                    longest = max(longest, j - i + 1)

        return longest

