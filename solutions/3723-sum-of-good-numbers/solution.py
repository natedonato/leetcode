class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        l = len(nums)
        good_sum = 0

        for i in range(0, l):
            if(i - k < 0 or nums[i - k] < nums[i]) and (i + k >= l or nums[i + k] < nums[i]):
                good_sum += nums[i]

        return good_sum
