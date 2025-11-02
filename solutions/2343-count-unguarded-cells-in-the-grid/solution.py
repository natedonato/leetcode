class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        self.grid = [ [0 for _ in range(n)] for _ in range(m)]    
        vects = [[0,1],[0,-1],[1,0],[-1,0]]

        for w in walls:
            self.grid[w[0]][w[1]] = 1

        for g in guards:
            self.grid[g[0]][g[1]] = 2

        for g in guards:
            self.grid[g[0]][g[1]] = 0
            for vect in vects:
                # move along direction until out of bounds or not zero
                curr = g[:]
                while curr[0] >= 0 and curr[1] >= 0 and curr[0] < m and curr[1] < n and self.grid[curr[0]][curr[1]] != 1 and self.grid[curr[0]][curr[1]] != 2:
                    self.grid[curr[0]][curr[1]] = 3
                    curr[0] += vect[0]
                    curr[1] += vect[1]    

            self.grid[g[0]][g[1]] = 2
                


        count = 0
        for r in range(m):
            for c in range(n):
                if self.grid[r][c] == 0:
                    count += 1

        return count

    
