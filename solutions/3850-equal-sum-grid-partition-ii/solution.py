class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        total_sum = 0
        m = len(grid)
        n = len(grid[0])

        total_counts = collections.Counter()

        for r in range(m):
            for c in range(n):
                total_sum += grid[r][c]
                total_counts[grid[r][c]] += 1

        part_sum = 0

        left_counts = collections.Counter()
        
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                left_counts[val] += 1
                part_sum += grid[r][c]

            target_sum = total_sum - part_sum

            if part_sum == target_sum:
                return True

            elif part_sum > target_sum:
                diff = part_sum - target_sum

                if left_counts[diff] > 0:
                    if r > 0 and n > 1:
                        return True

                    elif r > 0 and n == 1:
                        if grid[0][0] == diff or grid[r][0] == diff:
                            return True

                    elif r == 0:
                        if n > 1 and grid[0][0] == diff or grid[0][-1] == diff:
                            return True

            elif target_sum > part_sum:
                diff = target_sum - part_sum

                if total_counts[diff] - left_counts[diff] > 0:
                    if r < m - 1 - 1 and n > 1:
                        return True

                    elif r < m - 1 - 1 and n == 1:
                        if grid[r + 1][0] == diff or grid[m - 1][0] == diff:
                            return True
                    
                    elif r == m - 1 - 1:
                        if n > 1 and grid[m - 1][0] == diff or grid[m - 1][-1] == diff:
                            return True
        
        part_sum = 0
        left_counts = collections.Counter()
        
        for c in range(n):
            for r in range(m):
                val = grid[r][c]
                left_counts[val] += 1
                part_sum += grid[r][c]

            target_sum = total_sum - part_sum

            if part_sum == target_sum:
                return True

            elif part_sum > target_sum:
                diff = part_sum - target_sum

                if left_counts[diff] > 0:
                    if c > 0 and m > 1:
                        return True

                    elif c > 0 and m == 1:
                        if grid[0][0] == diff or grid[0][c] == diff:
                            return True

                    elif c == 0:
                        if m > 1 and grid[0][0] == diff or grid[-1][0] == diff:
                            return True

            elif target_sum > part_sum:
                diff = target_sum - part_sum

                if total_counts[diff] - left_counts[diff] > 0:
                    if c < n - 1 - 1 and m > 1:
                        return True

                    elif c < n - 1 - 1 and m == 1:
                        if grid[0][c + 1] == diff or grid[0][n - 1] == diff:
                            return True

                    elif c == n - 1 - 1:
                        if m > 1 and grid[0][n - 1] == diff or grid[-1][n - 1] == diff:
                            return True
        
                
        return False
            

