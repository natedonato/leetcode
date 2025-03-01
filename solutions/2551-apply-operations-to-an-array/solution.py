class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []

        for i in range(0,n):
            if i < n - 1 and nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

            if nums[i] != 0:
                output.append(nums[i])

        while(len(output) < n):
            output.append(0)

        return output
