class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        self.k = k
        self.nums = nums

        l = 0
        r = max(nums)

        while(l < r):
            mid = (r - l) // 2 + l
            if(self.canHitMin(mid)):
                r = mid
            else:
                l = mid + 1
        
        return l




    def canHitMin(self, minimum):
        count = 0
        i = 0
        l = len(self.nums)

        while i < l:
            if self.nums[i] <= minimum:
                count += 1
                if count >= self.k:
                    return True
                i += 2
            else:
                i += 1
        
        return False
        
