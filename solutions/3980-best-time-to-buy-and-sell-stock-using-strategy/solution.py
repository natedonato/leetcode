class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prefix_pos = [0]
        prefix_neg = [0]

        for i in range(len(prices)):
            prefix_pos.append(prefix_pos[-1] + prices[i])
            prefix_neg.append(prefix_neg[-1] + (prices[i] * strategy[i]))

        unmodified = prefix_neg[-1]
        best = unmodified

        for i in range(0, len(prefix_pos) - k):
            l = i
            mid = k//2 + i
            r = mid + k // 2

            lost_sum = prefix_neg[r] - prefix_neg[l]
            gained_sum = prefix_pos[r] - prefix_pos[mid]

            best = max(best, unmodified - lost_sum + gained_sum)

        return best
