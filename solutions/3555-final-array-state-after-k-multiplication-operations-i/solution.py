class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for x in range(0,k):
            min = None
            idx = -1
            for i, num in enumerate(nums):
                if min is None or num < min:
                    min = num
                    idx = i
            
            nums[idx] = nums[idx] * multiplier
        
        return nums
