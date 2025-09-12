class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vs = 'aeiou'
        for c in s:
            if c in vs:
                return True

        return False
