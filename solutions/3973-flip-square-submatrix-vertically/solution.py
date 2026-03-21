class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for r in range(k//2):
            for c in range(k):
                grid[x + r][y + c], grid[x + k - r - 1][y+c] = grid[x + k - r - 1][y+c], grid[x + r][y+c]

        return grid
