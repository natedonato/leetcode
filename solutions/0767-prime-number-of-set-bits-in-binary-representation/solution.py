class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            bits = i.bit_count()
            if self.isPrime(bits):
                count += 1

        return count
    
    def isPrime(self, num):
        if num < 2:
            return 0

        for i in range(2, num):
            if num % i == 0:
                return False

        return True
