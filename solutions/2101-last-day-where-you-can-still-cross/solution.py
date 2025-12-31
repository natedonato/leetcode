class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.max_days = len(cells)
        self.grid = [[len(cells)] * col for _ in range(row)]
        i = len(cells) - 1
        for cell in cells:
            self.grid[cell[0] - 1][cell[1] - 1] = i
            i -= 1

        l = 0
        r = len(cells)
        while l < r:
            mid = l + ((r-l) // 2)
            if self.canSolve(mid):
                l = mid + 1
            else:
                r = mid

        return l - 1
        
    def canSolve(self, day):
        limit = self.max_days - day
        top = []
        for c in range(len(self.grid[0])):
            if self.grid[0][c] < limit:
                top.append((0,c))
        seen = set(top)
        q = deque(top)

        while q:
            curr = q.popleft()
            if curr[0] == len(self.grid) - 1:
                return True
            neighbors = self.getNeighbors(curr)
            for n in neighbors:
                if n not in seen and self.grid[n[0]][n[1]] < limit:
                    seen.add(n)
                    q.append(n)

        return False

    def getNeighbors(self, point):
        r, c = point
        neighbors = []
        for vec in [[0,1],[0,-1],[1,0],[-1,0]]:
            r1 = r + vec[0]
            c1 = c + vec[1]
            if r1 >= 0 and c1 >= 0 and r1 < len(self.grid) and c1 < len(self.grid[0]):
                neighbors.append((r1,c1))

        return neighbors
