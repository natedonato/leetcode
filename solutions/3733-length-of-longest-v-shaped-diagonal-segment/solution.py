class Solution:
    direction_vects = [
        [-1,1],
        [1,1],
        [1,-1],
        [-1,-1]
    ]

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        self.grid = grid
        best_length = 0

        self.memo = {}

        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1:
                    for i in range(0,4):
                        length = self.traverse(r,c,i, False, 1)
                        best_length = max(best_length, length)

        return best_length
    
    def traverse(self, r, c, direction, has_turned = False, target_value = 1):
        key = (r, c, direction, has_turned, target_value)
        if key in self.memo:
            return self.memo[key]

        if self.oob(r,c):
            self.memo[key] = 0
            return 0

        val = self.grid[r][c]
        if (val != target_value):
            self.memo[key] = 0
            return 0

        if target_value == 1 or target_value == 0:
            target_value = 2
        elif target_value == 2:
            target_value = 0

        next_r = r + Solution.direction_vects[direction][0]
        next_c = c + Solution.direction_vects[direction][1]

        subproblem_solution = self.traverse(next_r, next_c, direction, has_turned, target_value)
        
        if has_turned == False:
            turned_direction = self.rotate(direction)
            next_r_turned = r + Solution.direction_vects[turned_direction][0]
            next_c_turned = c + Solution.direction_vects[turned_direction][1]
            subproblem_solution = max(subproblem_solution, self.traverse(next_r_turned, next_c_turned, turned_direction, True, target_value))

        ans = 1 + subproblem_solution
        self.memo[key] = ans

        return ans

    def rotate(self, idx):
        idx += 1
        idx %= 4
        return idx

    def oob(self, r,c):
        if r < 0 or c < 0 or r >= len(self.grid) or c >= len(self.grid[0]):
            return True
        return False
