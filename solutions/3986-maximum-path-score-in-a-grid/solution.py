class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[-math.inf] * (k + 1) for _ in range(m)]  for _ in range(n)]
        
        dp[0][0][0] = 0

        for r in range(n):
            for c in range(m):
                val = grid[r][c]
                cost = 1 if val != 0 else 0

                if r > 0:
                    prev = dp[r - 1][c]
                    for prev_cost in range(len(prev)):
                        next_cost = prev_cost + cost
                        if next_cost <= k:
                            dp[r][c][next_cost] = max(dp[r][c][next_cost], prev[prev_cost] + val)
                
                if c > 0:
                    prev = dp[r][c - 1]
                    for prev_cost in range(len(prev)):
                        next_cost = prev_cost + cost
                        if next_cost <= k:
                            dp[r][c][next_cost] = max(dp[r][c][next_cost], prev[prev_cost] + val) 

        val = max(dp[n-1][m-1])

        return -1 if val == -math.inf else val


[
    [[0, -inf]], 
    [[-inf, -inf]], 
    [[-inf, -inf]], 
    [[-inf, -inf]]
]
