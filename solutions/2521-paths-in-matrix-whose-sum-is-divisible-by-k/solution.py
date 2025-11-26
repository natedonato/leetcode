class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        overflow = 1_000_000_000 + 7

        mods = [ [{} for _ in range(n)] for _ in range(m) ]
        

        mods[0][0][grid[0][0] % k] = 1


        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                mod = mods[r][c]
                if r > 0:
                    left = mods[r-1][c]
                    for remainder, count in left.items():
                        next_remainder = (remainder + val) % k
                        if next_remainder not in mod:
                            mod[next_remainder] = 0
                        mod[next_remainder] += count
                        mod[next_remainder] %= overflow
                
                if c > 0:
                    up = mods[r][c-1]
                    for remainder, count in up.items():
                        next_remainder = (remainder + val) % k
                        if next_remainder not in mod:
                            mod[next_remainder] = 0
                        mod[next_remainder] += count
                        mod[next_remainder] %= overflow

        if 0 not in mods[m-1][n-1]:
            return 0
        else:
            return mods[m-1][n-1][0]
