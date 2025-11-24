class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        c = 0
        out = []
        for n in nums:
            c = c << 1
            c += n
            out.append(c%5==0)

        return out
