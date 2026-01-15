class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        max_h = 1
        max_v = 1

        hBars.sort()
        vBars.sort()
        count = 1
        for i, bar in enumerate(hBars):
            continuous = False
            if not (i > 0 and bar - 1 == hBars[i-1]):
                count = 1

            count += 1
            max_h = max(count, max_h)

        count = 1
        for i, bar in enumerate(vBars):
            continuous = False
            if not (i > 0 and bar - 1 == vBars[i-1]):
                count = 1

            count += 1
            max_v = max(count, max_v)

        return min(max_h, max_v) ** 2
