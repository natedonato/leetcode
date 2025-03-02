class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(int(c) for c in s)
        while len(s) > 2:
            first = s[0]
            second = s[1]

            for i in range(0, len(s) - 1):
                s[i] = (first + second) % 10
                if( i + 2 < len(s)):
                    first = s[i + 1]
                    second = s[i + 2]
            s.pop()

        return s[0] == s[1]
