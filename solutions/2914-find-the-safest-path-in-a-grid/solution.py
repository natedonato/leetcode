class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        self.m = m
        self.n = n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r,c))
                    grid[r][c] = 0
                else:
                    grid[r][c] = -1

        dist = 1

        while q:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()

                for n in self.getNeighbors(r,c):
                    r1, c1 = n
                    if grid[r1][c1] == -1:
                        grid[r1][c1] = dist
                        q.append(n)
            
            dist += 1

        start_val = grid[0][0]

        pqueue = [(start_val, 0, 0)]
        min_val = start_val

        seen = set()
        seen.add((0,0))
        while pqueue:
            current = heapq.heappop_max(pqueue)
            val, r, c = current
            min_val = min(min_val, val)
            if r == self.m - 1 and c == self.n - 1:
                return min_val
            
            neighbors = self.getNeighbors(r,c)

            for n in neighbors:
                if n not in seen:
                    seen.add(n)
                    r1,c1 = n
                    heapq.heappush_max(pqueue, (grid[r1][c1], r1, c1))

        return -1 

    def getNeighbors(self, r, c):
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        out = []
        for d in dirs:
            r1 = r + d[0]
            c1 = c + d[1]

            if r1 >= 0 and c1 >= 0 and r1 < self.m and c1 < self.n:
                out.append((r1,c1))

        return out
