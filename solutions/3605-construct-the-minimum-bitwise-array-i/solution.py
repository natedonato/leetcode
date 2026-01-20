class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        out = []
        for num in nums:
            found = False
            for i in range(num):
                if i | i + 1 == num:
                    out.append(i)
                    found = True
                    break

            if not found:
                out.append(-1)

        return out
