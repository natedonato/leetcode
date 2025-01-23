class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0
        
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if rows[r] > 1:
                        count += 1
                    elif cols[c] > 1:
                        count += 1
                        
        return count 
   
        
