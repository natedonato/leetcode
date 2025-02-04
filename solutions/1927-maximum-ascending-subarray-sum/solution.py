class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        prev = nums[0]
        current_sum = max_sum

        for i in range (1, len(nums)):
            next_el = nums[i]

            if next_el > prev:
                current_sum += next_el
            else:
                current_sum = next_el

            prev = next_el
            max_sum = max(max_sum, current_sum)

        return max_sum
