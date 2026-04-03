# 2, 4
# 0 2 6
import bisect

class Solution:
    # find num walls within bounds inclusive

    def findWalls(self, left_bound, right_bound):
        left_idx = bisect.bisect_left(self.walls, left_bound)
        right_idx = bisect.bisect_right(self.walls, right_bound)

        return right_idx - left_idx


    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        self.walls = walls
        self.walls.sort()
        
        # [[max_score_left, bot_position], [max_score_right, max_position_reached_by_shoot_right]]
        dp = [[[0,0],[0,0]] for _ in range(len(robots))]

        bots = list(zip(robots,distance))
        bots.sort()

        for i in range(len(bots)):

            bot_pos, bot_range = bots[i]
            if i > 0:
                prev = dp[i-1]
            else:
                prev = [[0,0],[0,0]]

            if i < len(bots) - 1:
                next_bot_pos = bots[i+1][0] - 1
            else:
                next_bot_pos = math.inf

            # case for aim right right
            range_right =  min(bot_pos + bot_range, next_bot_pos)
            can_hit_right = self.findWalls(bot_pos, range_right)
            dp[i][1] = [max(prev[0][0], prev[1][0]) + can_hit_right, range_right]

            # case for aim left
            range_left_1 = max(bot_pos - bot_range, prev[0][1] + 1)
            range_left_2 = max(bot_pos - bot_range, prev[1][1] + 1)
            can_hit_left_1 = self.findWalls(range_left_1, bot_pos)
            can_hit_left_2 = self.findWalls(range_left_2, bot_pos)

            dp[i][0] = [max(can_hit_left_1 + prev[0][0], can_hit_left_2 + prev[1][0]), bot_pos]

        return max(dp[-1][0][0], dp[-1][1][0])


