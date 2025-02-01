class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        expected = nums[0] % 2 == 0
        
        for num in nums:
            if (num % 2 == 0) != expected:
                return False
            
            expected = not expected
            
        return True 
