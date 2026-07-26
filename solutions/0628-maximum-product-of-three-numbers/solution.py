class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        # largest 3
        max_prod = nums[-1] * nums[-2] * nums[-3]

        # two most negative and largest positive
        max_prod = max(max_prod, nums[0] * nums[1] * nums[-1])

        return max_prod
