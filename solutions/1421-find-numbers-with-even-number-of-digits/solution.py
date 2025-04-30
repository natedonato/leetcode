class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            if self.countDigits(num) % 2 == 0:
                total += 1

        return total

    def countDigits(self, num: int):
        digits = 0
        while num > 0:
            digits += 1
            num //= 10
        return digits
