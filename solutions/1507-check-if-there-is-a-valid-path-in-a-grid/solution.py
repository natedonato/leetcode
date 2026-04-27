class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.grid = grid

        self.streets = {
            1: [[0, 1], [0, -1]],
            2: [[-1, 0], [1, 0]],
            3: [[0, -1], [1, 0]],
            4: [[0, 1], [1, 0]],
            5: [[0, -1], [-1, 0]],
            6: [[0, 1], [-1, 0]],
        }

        q = deque()
        q.append((0, 0))
        seen = set()

        while q:
            point = q.popleft()
            r, c = point

            if r == len(self.grid) - 1 and c == len(self.grid[0]) - 1:
                return True
            seen.add(point)

            for n in self.getNeighbors(r, c):

                if n not in seen and point in self.getNeighbors(n[0], n[1]):
                    q.append(n)

        return False

    def getNeighbors(self, r, c):
        val = self.grid[r][c]
        vects = self.streets[val]

        neighbors = []

        for vect in vects:
            r1 = r + vect[0]
            c1 = c + vect[1]
            if r1 >= 0 and r1 < len(self.grid) and c1 >= 0 and c1 < len(self.grid[0]):
                neighbors.append((r1, c1))

        return neighbors

