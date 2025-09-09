class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n = len(grid)

        if grid[0][0] == 1:
            return -1

        q = deque([(0,0,1)])
        visited = set([(0,0)])

        while q:
            curr = q.popleft()
            (r,c,dist) = curr
            if r == self.n-1 and c == self.n-1:
                return dist
            neighbors = self.getZeroNeighbors(r,c)

            for n in neighbors:
                if n not in visited:
                    visited.add(n)
                    q.append((n[0],n[1], dist+1))
        
        return -1

    def getZeroNeighbors(self, r, c):
        neighbors = []
        for x in range(-1,2):
            for y in range(-1,2):
                if x == 0 and y == 0:
                    continue
                
                r1 = r + x
                c1 = c + y

                if r1 >= 0 and c1 >= 0 and r1 < self.n and c1 < self.n and self.grid[r1][c1] == 0:
                    neighbors.append((r1,c1))

        return neighbors
