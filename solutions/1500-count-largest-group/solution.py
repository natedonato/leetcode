class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = collections.defaultdict(int)
        best = 0

        for i in range(1,n+1):
            digit_sum = self.sumDigits(i)
            
            counts[digit_sum] += 1
            if counts[digit_sum] > best:
                best = counts[digit_sum]
        
        groups = 0
        for val in counts.values():
            if val == best:
                groups += 1

        return groups

    def sumDigits(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum
