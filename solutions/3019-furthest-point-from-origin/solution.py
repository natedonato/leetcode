class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = 0
        r = 0

        for c in moves:
            if c == "R": 
                r += 1
                l -= 1
            elif c == "L":
                l += 1
                r -= 1
            else: 
                l += 1
                r += 1

        return max(l,r)
