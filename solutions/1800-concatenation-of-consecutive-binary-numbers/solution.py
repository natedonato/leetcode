class Solution:
    def concatenatedBinary(self, n: int) -> int:
        out = []
        for i in range(n+1):
            out.append(bin(i)[2:])

        return int("".join(out),2) % 1_000_000_007
