class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s = nums[0]
        min_el = nums[1]
        min_cost = math.inf

        for i in range(2, len(nums)):
            n = nums[i]
            min_cost = min(min_cost, s + min_el + n)
            min_el = min(min_el, n)

        return min_cost
