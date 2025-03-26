class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        m = len(grid)
        n = len(grid[0])
        for r in range(0, m):
            for c in range(0, n):
                arr.append(grid[r][c])
        
        arr.sort()

        mid = arr[len(arr)//2]
        count = 0

        for el in arr:
            diff = abs(el - mid)
            if diff % x != 0:
                return -1
            else:
                count += diff // x

        return count

