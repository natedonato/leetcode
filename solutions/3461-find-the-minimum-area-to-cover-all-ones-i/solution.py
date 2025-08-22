class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minr = math.inf
        minc = math.inf
        maxr = -1
        maxc = -1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    minr = min(minr, r)
                    maxr = max(maxr, r)
                    minc = min(minc, c)
                    maxc = max(maxc, c)

        return (maxr - minr + 1) * (maxc - minc + 1)
