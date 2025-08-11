class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7

        powers = []
        current_power_value = 1
        while n > 0:
            next_bit = n & 1
            n = n >> 1
            if next_bit != 0:
                powers.append(current_power_value)
            current_power_value *= 2
        prefix = [1]

        for power in powers:
            prefix.append(prefix[-1] * power)
        
        out = []
        for query in queries:
            left = query[0]
            right = query[1]
            quotient = prefix[right+1] // prefix[left]

            out.append(quotient % mod)

        return out

