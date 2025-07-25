class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_el = nums[0]
        seen = set()
        max_sum = 0

        for num in nums:
            if num not in seen:
                seen.add(num)
                max_el = max(num, max_el)
                if num > 0:
                    max_sum += num

        if max_el < 0:
            return max_el

        return max_sum
