class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_dif = math.inf
        nums.sort()

        for i in range(len(nums) - k + 1):
            l = nums[i]
            r = nums[i+k-1]

            min_dif = min(min_dif, r - l)

        return min_dif
