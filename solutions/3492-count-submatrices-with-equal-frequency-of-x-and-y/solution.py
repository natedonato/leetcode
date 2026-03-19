class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pre = [[[0,0] for _ in range(n)] for _ in range(m) ]

        count = 0
        for r in range(m):
            current_row_x = 0
            current_row_y = 0
            for c in range(n):
                val = grid[r][c]
                if val == "X":
                    current_row_x += 1
                elif val == "Y":
                    current_row_y += 1
                
                if r > 0:
                    above_x, above_y = pre[r-1][c]
                else:
                    above_x = 0
                    above_y = 0

                current = [current_row_x + above_x, current_row_y + above_y]

                if current[0] > 0 and current[0] == current[1]:
                    count += 1 
                pre[r][c] = current

        return count
