class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            next_s = []

            for i in range(1, len(s)):
                p = s[i - 1]
                c = s[i]
                next_char = (int(p) + int(c)) % 10
                next_s.append(str(next_char))

            s = "".join(next_s)

        return s[0] == s[1]
