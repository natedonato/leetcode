class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        n = len(grid)

        for row in grid:
            for el in row:
                if el in seen:
                    a = el
                else:
                    seen.add(el)

        for i in range(1, n*n + 1):
            if i not in seen:
                return [a, i]
