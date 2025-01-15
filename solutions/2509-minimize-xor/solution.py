class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_bits = bin(num2).count("1")
        ans = num1
        ans_bits = bin(num1).count("1")

        while ans_bits < num_bits:
            ans = ans | (ans + 1)
            ans_bits += 1

        while ans_bits > num_bits:
            ans = ans & (ans - 1)
            ans_bits -= 1

        return ans
