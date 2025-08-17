class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1
        running_sum = 0

        for i in range(1, n + 1):
            if i - maxPts - 1 >= 0 and i - maxPts - 1 < k:
                running_sum -= dp[i- maxPts - 1]

            if i - 1 < k:
                running_sum += dp[i-1]

            dp[i] += running_sum / maxPts

        answer = 0

        for i in range(k, n + 1):
            answer += dp[i]

        return answer

