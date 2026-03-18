class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix = [ [ 0 for _ in range(n + 1)] for _ in range(m + 1)]

        count = 0
        for r in range(m):
            current_row_sum = 0
            for c in range(n):
                prev_col_sum = prefix[r][c+1]
                current_row_sum += grid[r][c] 
                prefix[r+1][c+1] = current_row_sum + prev_col_sum
                if prefix[r+1][c+1] <= k:
                    count += 1
    
        return count

