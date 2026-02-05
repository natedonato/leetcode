class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [0] * l
        for i, num in enumerate(nums):
            j = (i + num) % l
            result[i] = nums[j]

        return result
            
