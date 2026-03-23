class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        maxes = [[-math.inf for _ in range(n)]  for _ in range(m)]
        mins = [[math.inf for _ in range(n)]  for _ in range(m)]

        maxes[0][0] = grid[0][0]
        mins[0][0] = grid[0][0]

        for r in range(m):
            for c in range(n):
                val = grid[r][c]

                if r > 0:
                    prev_max = maxes[r-1][c]
                    prev_min = mins[r-1][c]

                    maxes[r][c] = max(maxes[r][c], prev_max * val, prev_min * val)
                    mins[r][c] = min(mins[r][c], prev_max * val, prev_min * val) 
                if c > 0:
                    prev_max = maxes[r][c-1]
                    prev_min = mins[r][c-1]

                    maxes[r][c] = max(maxes[r][c], prev_max * val, prev_min * val)
                    mins[r][c] = min(mins[r][c], prev_max * val, prev_min * val) 

        best = maxes[m-1][n-1]
        if best < 0:
            return -1
        return best % 1_000_000_007
