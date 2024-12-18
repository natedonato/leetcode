class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [];
        for idx, price in enumerate(prices):
            while len(stack) > 0 and prices[stack[-1]] >= price:
                prices[stack[-1]] -= price
                stack.pop()
            
            stack.append(idx)
            
        return prices
            
        
