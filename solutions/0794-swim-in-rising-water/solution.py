class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.grid = grid
        m = len(grid)
        n = len(grid[0])

        queued = set()
        min_time = 0
        q = []
        heapq.heappush(q, (grid[0][0],(0,0)))
        queued.add((0,0))

        while q:
            [t, (r, c)] = heapq.heappop(q)
            
            min_time = max(min_time, t)
            if r == m - 1 and c == n - 1:
                return min_time
            
            neighbors = self.getNeighbors(r,c)

            for neighbor in neighbors:
                if neighbor not in queued:
                    queued.add(neighbor)
                    v = grid[neighbor[0]][neighbor[1]]
                    heapq.heappush(q,(v, neighbor))

    def getNeighbors(self, r, c):
        out = []
        vects = [[0,1],[0,-1],[1,0],[-1,0]]
        for v in vects:
            r1 = r + v[0]
            c1 = c + v[1]

            if r1 >= 0 and c1 >= 0 and r1 < len(self.grid) and c1 < len(self.grid[0]):
                out.append((r1,c1))
        
        return out
