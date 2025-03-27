class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0] * l
        
        if(l == 1):
            return nums[0]
        if(l == 2):
            return max(nums[0], nums[1])

        dp[0] = nums[0]
        dp[1] = nums[1]


        for i in range(1, l):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        print(dp)

        return dp[-1]
