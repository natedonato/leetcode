class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for e in row:
                if e < 0:
                    count += 1

        return count
