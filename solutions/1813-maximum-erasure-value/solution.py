class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        current_sum = 0
        max_sum = 0
        seen = {}

        for r in range(0, len(nums)):
            next_num = nums[r]
            if next_num in seen:
                prev = seen[next_num]
                while l <= prev:
                    current_sum -= nums[l]
                    l += 1
                

            current_sum += next_num
            seen[next_num] = r
            max_sum = max(max_sum, current_sum)

        return max_sum
