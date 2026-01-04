class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            s = set()
            for i in range(1, ceil(math.sqrt(num)) +1):
                if num % i == 0:
                    s.add(i)
                    s.add(num //i)

            if len(s) == 4:
                total += sum(s)

        return total
