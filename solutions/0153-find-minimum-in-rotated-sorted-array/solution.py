class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (r - l)//2 + l

            if nums[mid] < nums[0]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
