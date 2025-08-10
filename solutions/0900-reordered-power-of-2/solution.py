class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        key = ''.join(sorted(str(n)))

        for i in range(31):
            if key == ''.join(sorted(str(2**i))):
                return True

        return False
