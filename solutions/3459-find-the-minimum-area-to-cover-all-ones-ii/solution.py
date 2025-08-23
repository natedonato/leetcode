class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        print('start')
        self.grid = grid
        minimum_possible_area = math.inf
        n = len(grid)
        m = len(grid[0])

        total_one_count = 0
        for r in range(0,n):
            for c in range(0,m):
                if grid[r][c] == 1:
                    total_one_count += 1
        
        # vertical first box
        for i in range(0, m - 1):
            first_area = self.minimumArea(0, n-1, 0, i)
            if first_area[0] == 0:
                continue
            
            # vertical second boxes
            for j in range(i+1, m-1):
                second_area = self.minimumArea(0, n - 1, i + 1, j)
                third_area = self.minimumArea(0, n - 1, j + 1, m-1)

                if second_area[0] == 0 or third_area[0] == 0 or first_area[1] + second_area[1] + third_area[1] != total_one_count:
                    continue
                
                minimum_possible_area = min(minimum_possible_area, first_area[0] + second_area[0] + third_area[0])
            
            #horizontal second boxes
            for k in range(0,n-1):
                second_area = self.minimumArea(0, k, i + 1, m-1)
                third_area = self.minimumArea(k+1, n - 1, i+1, m-1)

                if second_area[0] == 0 or third_area[0] == 0 or first_area[1] + second_area[1] + third_area[1] != total_one_count:
                    continue
                
                minimum_possible_area = min(minimum_possible_area, first_area[0] + second_area[0] + third_area[0])

        # horizontal first box
        for r in range(0, n - 1):
            first_area = self.minimumArea(0, r, 0, m-1)

            # horizontal second boxes
            for k in range(r+1,n-1):
                second_area = self.minimumArea(r+1, k, 0, m-1)
                third_area = self.minimumArea(k+1, n - 1, 0, m-1)

                if second_area[0] == 0 or third_area[0] == 0 or first_area[1] + second_area[1] + third_area[1] != total_one_count:
                    continue
                
                minimum_possible_area = min(minimum_possible_area, first_area[0] + second_area[0] + third_area[0])

            #vertical second boxes
            for j in range(0, m-1):
                second_area = self.minimumArea(r+1, n - 1, 0, j)
                third_area = self.minimumArea(r+1, n - 1, j+1, m-1)

                if second_area[0] == 0 or third_area[0] == 0 or first_area[1] + second_area[1] + third_area[1] != total_one_count:
                    continue
                
                minimum_possible_area = min(minimum_possible_area, first_area[0] + second_area[0] + third_area[0])

        # horizontal first box upsidown
        for r in reversed(range(1,n)):
            first_area = self.minimumArea(r, n-1, 0, m-1)
            
            #vertical second boxes
            for j in range(0, m-1):
                second_area = self.minimumArea(0, r - 1, 0, j)
                third_area = self.minimumArea(0, r - 1, j+1, m-1)

                if second_area[0] == 0 or third_area[0] == 0 or first_area[1] + second_area[1] + third_area[1] != total_one_count:
                    continue
                
                minimum_possible_area = min(minimum_possible_area, first_area[0] + second_area[0] + third_area[0])

        #vertical first box RTL
        for c in reversed(range(1,m)):
            first_area = self.minimumArea(0,n-1,c,m-1)
            
            #horizontal second boxes
            for k in range(0,n-1):
                second_area = self.minimumArea(0, k, 0, c-1)
                third_area = self.minimumArea(k+1, n - 1, 0, c-1)

                if second_area[0] == 0 or third_area[0] == 0 or first_area[1] + second_area[1] + third_area[1] != total_one_count:
                    continue
                
                minimum_possible_area = min(minimum_possible_area, first_area[0] + second_area[0] + third_area[0])

        return minimum_possible_area


    def minimumArea(self, start_r, end_r, start_c, end_c) -> int:
        minr = end_r + 1
        minc = end_c + 1
        maxr = start_r - 1
        maxc = start_c - 1
        one_count = 0

        for r in range(start_r, end_r + 1):
            for c in range(start_c, end_c + 1):
                if self.grid[r][c] == 1:
                    one_count += 1
                    minr = min(minr, r)
                    maxr = max(maxr, r)
                    minc = min(minc, c)
                    maxc = max(maxc, c)

        if one_count == 0:
            return [0,0]

        return [(maxr - minr + 1) * (maxc - minc + 1), one_count]
