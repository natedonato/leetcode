class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                
                if r + 1 < m:
                    dp[r+1][c] += dp[r][c]
                if c + 1 < n:
                    dp[r][c+1] += dp[r][c]

        return dp[m-1][n-1]
