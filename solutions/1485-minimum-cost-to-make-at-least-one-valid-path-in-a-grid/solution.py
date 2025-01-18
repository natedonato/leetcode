class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        dirs = {
            1: [0,1],
            2: [0, -1],
            3: [1,0],
            4: [-1,0]
        }

        start = (0,0)
        pq = []
        m = len(grid) - 1
        n = len(grid[0]) - 1
        visited = set()

        heapq.heappush(pq, (0, start))

        while pq:
            cost, current = heapq.heappop(pq)
            if current[0] == m and current[1] == n:
                return cost
            if current in visited:
                continue
            else:
                visited.add(current)

            
            sign = grid[current[0]][current[1]]
            for i in range(1,5):
                nextPoint = (current[0] + dirs[i][0], current[1] + dirs[i][1])
                if nextPoint[0] < 0 or nextPoint[1] < 0 or nextPoint[0] > m or nextPoint[1] > n:
                    continue

                if sign == i:
                    heapq.heappush(pq, (cost, nextPoint))
                else:
                    heapq.heappush(pq, (cost + 1, nextPoint))

        
        return -1
