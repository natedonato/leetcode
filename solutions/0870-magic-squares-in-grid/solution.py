class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        self.grid = grid
        count = 0
        for r in range(0, len(grid) - 2):
            for c in range(0, len(grid[0]) - 2):
                valid = self.check(r,c)
                print(r, c, valid)
                if valid:
                    count += 1

        return count

    def check(self, r, c):
        rsums = [0, 0, 0]
        csums = [0, 0, 0]
        nums = [0] * 9
        diag_left = 0
        diag_right = 0

        for dr in [0,1,2]:
            for dc in [0,1,2]:
                val = self.grid[r + dr][c + dc]
                if val > 9 or val <= 0 or nums[val - 1] != 0:
                    return False
                nums[val - 1] = 1
                rsums[dr] += val
                csums[dc] += val
                if dr == dc:
                    diag_left += val
                if dr + dc == 2:
                    diag_right += val

        s = diag_left
        if s != diag_right:
            return False
        for rs in rsums[1:]:
            if rs != s:
                return False
        for cs in csums:
            if cs != s:
                return False

        return True

