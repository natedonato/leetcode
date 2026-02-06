class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        remain = 0
        nums.sort()

        l = 0
        r = 0
        while (r < len(nums)):
            while nums[l] * k < nums[r]:
                l += 1
            remain = max(remain, r - l + 1)
            r += 1

        return len(nums) - remain
