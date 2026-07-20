class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        self.m = len(grid)
        self.n = len(grid[0])
        total_len = self.m * self.n
        k %= total_len

        out = [[None for _ in range(self.n)] for _ in range(self.m)]

        for r in range(self.m):
            for c in range(self.n):
                idx = self.coordToFlat(r,c)
                idx += k
                idx %= total_len
                new_r, new_c = self.flatToCoord(idx)
                out[new_r][new_c] = grid[r][c]

        return out

    def coordToFlat(self, r, c):
        return (r * self.n) + c

    def flatToCoord(self, idx):
        r = idx // self.n
        c = idx % self.n
        return(r, c)

