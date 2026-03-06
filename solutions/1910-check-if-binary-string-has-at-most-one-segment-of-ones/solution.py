class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen = False
        for c in s:
            if c == "0":
                seen = True
            else:
                if seen:
                    return False

        return True
