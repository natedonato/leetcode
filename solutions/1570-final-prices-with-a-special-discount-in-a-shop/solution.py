class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # (price, index)
        s = []

        for i in range(len(prices)):
            price = prices[i]

            while s and price <= s[-1][0]:
                (prev_price, prev_index) = s.pop()
                prices[prev_index] = prev_price - price

            s.append((price, i))

        return prices
