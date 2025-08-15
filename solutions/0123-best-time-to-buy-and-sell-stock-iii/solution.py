class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = prices[0]
        max_profit_left = [0]
        for i in range(1, len(prices)):
            next_stock = prices[i]
            next_profit = max(prices[i] - left_min, max_profit_left[-1])
            max_profit_left.append(next_profit)
            left_min = min(left_min, next_stock)

        total_max = max_profit_left[-1]
        
        right_max = prices[-1]
        right_max_profit = 0

        for i in reversed(range(0, len(prices)-1)):
            prev_stock = prices[i]

            current_right_profit = right_max - prev_stock
            right_max_profit = max(right_max_profit, current_right_profit)
            current_left_profit = max_profit_left[i]
            total_max = max(total_max, right_max_profit + current_left_profit)

            right_max = max(right_max, prev_stock)

        return total_max
