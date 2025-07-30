class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)

        i = 0
        current = 0
        best = 0
        while i < len(nums):
            if nums[i] == maximum:
                current += 1
                best = max(best, current)
            else:
                current = 0
            i += 1

        return best
