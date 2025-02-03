class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        length_increasing = 1
        length_decreasing = 1
        max_len = 1

        for i in range(1, len(nums)):
            if nums[i] > prev:
                length_increasing += 1
                length_decreasing = 1
                max_len = max(length_increasing, max_len)
            elif nums[i] < prev:
                length_decreasing += 1
                length_increasing = 1
                max_len = max(length_decreasing, max_len)
            else:
                length_increasing = length_decreasing = 1
            
            prev = nums[i] 

        prev = nums[0]
        length = 1

        return max_len
