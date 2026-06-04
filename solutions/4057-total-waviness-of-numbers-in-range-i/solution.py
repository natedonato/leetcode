class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0

        for i in range(num1, num2+1):
            count += self.hasPeak(i)

        return count

    def hasPeak(self, num):
        waviness = 0
        digits = []
        
        while num > 0:
            digits.append(num % 10)
            num //= 10

        for i in range(1, len(digits) - 1):
            if (digits[i] > digits[i-1] and digits[i] > digits[i+1]) or (digits[i] < digits[i-1] and digits[i] < digits[i+1]):
                waviness += 1

        return waviness
