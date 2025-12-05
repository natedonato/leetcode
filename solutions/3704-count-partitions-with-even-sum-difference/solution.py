class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        lsum = 0
        rsum = sum(nums)

        for i in range(len(nums) - 1):
            n = nums[i]
            lsum += n
            rsum -= n

            if (rsum - lsum) % 2 == 0:
                count += 1

        return count
