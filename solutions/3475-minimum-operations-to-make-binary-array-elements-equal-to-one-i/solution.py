class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(0,len(nums) - 2):
            if nums[i] == 0:
                count += 1
                nums[i] = 1
                nums[i+1] = self.flip(nums[i+1])
                nums[i+2] = self.flip(nums[i+2])
    
        if nums[-1] == 1 and nums[-2] == 1:
            return count
        return -1
        
    def flip(self, b):
        if b == 1:
            return 0
        return 1
