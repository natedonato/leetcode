class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for r in range(0,m):
            for c in range(0,n):
                if c + 1 < n:
                    dp[r][c + 1] += dp[r][c]
                if r + 1 < m:
                    dp[r + 1][c] += dp[r][c]

        return dp[m-1][n-1]
