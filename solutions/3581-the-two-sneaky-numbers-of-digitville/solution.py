class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        out = []
        for n in nums:
            if n in s:
                out.append(n)
            else:
                s.add(n)

        return out
