class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l = 0
        r = 0
        count = 0

        while l < len(prices):
            while r + 1 < len(prices) and prices[r + 1] == prices[r] - 1:
                r += 1

            while l <= r:
                count += r - l + 1
                l += 1
            
            l = r + 1
            r = l

        return count
