class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if(r == 0 and c == 0):
                    dp[r][c] = grid[r][c]
                elif(r == 0):
                    dp[r][c] = grid[r][c] + dp[r][c-1]
                elif(c == 0):
                    dp[r][c] = grid[r][c] + dp[r-1][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])

        return dp[m-1][n-1]
