class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ["0"]

        while len(s) < k:
            prev = len(s)
            s += "1"
            for c in reversed(range(prev)):
                if s[c] == "1":
                    s.append("0")
                else:
                    s.append("1")

        return s[k - 1]
