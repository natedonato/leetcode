class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_color = None
        max_sub_cost = 0
        total = 0

        for i in range(len(colors)):
            color = colors[i]
            cost = neededTime[i]

            if color != prev_color:
                max_sub_cost = cost
                prev_color = color
            else:
                total += min(max_sub_cost, cost)
                max_sub_cost = max(max_sub_cost, cost)

        return total
