class Solution:
    def isGood(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        m = len(nums) - 1

        for n in nums:
            if n < 0 or n > m:
                return False
                
            if n == m and c[n] != 2:         
                return False
            elif n != m and c[n] != 1:
                return False

        return True
