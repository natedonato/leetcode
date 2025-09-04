class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        r = abs(z-x) - abs(z-y)

        if r > 0:
            return 2
        elif r < 0:
            return 1
        else:
            return 0
