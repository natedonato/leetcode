class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        mc = 0
        for n in nums:
            if n == 1:
                count += 1
                mc = max(mc, count)
            else:
                count = 0
        return mc
