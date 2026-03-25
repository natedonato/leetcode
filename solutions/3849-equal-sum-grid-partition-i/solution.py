class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total_sum = 0
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                total_sum += grid[r][c]

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        part_sum = 0
        
        for r in range(m):
            for c in range(n):
                part_sum += grid[r][c]
            if part_sum == target_sum:
                return True
            elif part_sum > target_sum:
                break
                
        part_sum = 0
        for c in range(n):
            for r in range(m):
                part_sum += grid[r][c]
            if part_sum == target_sum:
                return True
            elif part_sum > target_sum:
                break
                
        return False
            

