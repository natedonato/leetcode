class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ""

        chars = set(s)

        for i, c in enumerate(s):
            if c.swapcase() not in s:
                left = s[:i]
                right = s[i+1:]

                left_solution = self.longestNiceSubstring(left)
                right_solution = self.longestNiceSubstring(right)

                if len(right_solution) > len(left_solution):
                    return right_solution
                else:
                    return left_solution

        return s

