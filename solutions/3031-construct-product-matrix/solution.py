class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        
        right_prod = [[0 for _ in range(n)] for _ in range(m)]
        running_prod = 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                right_prod[r][c] = running_prod
                running_prod *= grid[r][c]
                running_prod %= 12345
        
        running_prod = 1

        for r in range(m):
            for c in range(n):
                val = grid[r][c]

                grid[r][c] = (running_prod * right_prod[r][c]) % 12345
                running_prod *= val
                running_prod %= 12345

        return grid


