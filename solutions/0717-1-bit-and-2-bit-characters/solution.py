class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        onebit = True
        while i < len(bits):
            if bits[i] == 0:
                onebit = True
                i += 1
            else:
                onebit = False
                i += 2
        return onebit
