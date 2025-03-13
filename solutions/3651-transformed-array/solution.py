class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        output = []
        for i, num in enumerate(nums):
            index = (i + num)
            index = index % len(nums)
            output.append(nums[index])
        
        return output
