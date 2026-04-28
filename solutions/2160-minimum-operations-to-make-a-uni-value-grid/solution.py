class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = [el for row in grid for el in row]
        a.sort()

        med = a[len(a) // 2]

        remain = med % x
        ops = 0

        for el in a:
            if el % x != remain:
                return -1
            
            diff = abs(med - el)
            ops += diff // x

        return ops
