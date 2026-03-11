class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        out = 0
        digit = 0
        
        while n > 0:
            next_bit = n % 2
            if next_bit == 0:
                out += 1 << digit

            digit += 1
            n //= 2

        return out
