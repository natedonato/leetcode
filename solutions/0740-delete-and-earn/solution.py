class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        m = max(nums)
        dp = [0] * (m + 1)
        dp[1] = counts[1] 

        for i in range(2, m + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * counts[i])

        return dp[-1]
