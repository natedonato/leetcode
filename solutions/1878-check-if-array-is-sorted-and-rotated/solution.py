class Solution:
    def check(self, nums: List[int]) -> bool:
        count = len(nums)
        while nums[0] >= nums[-1] and count >= 0:
            nums = [nums[-1]] + nums[:-1]
            count -= 1

        prev = -1
        for num in nums:
            if num < prev:
                return False
            prev = num

        return True
