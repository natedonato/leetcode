class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        MODULO = (10 ** 9) + 7

        l = 0
        r = len(nums) - 1

        while(l <= r):
            if nums[l] + nums[r] > target:
                r -= 1
                continue
            
            count += 2 ** (r - l)
            count %= MODULO

            l += 1

        return count
        
