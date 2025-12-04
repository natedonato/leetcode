class Solution:
    def countCollisions(self, directions: str) -> int:
        moving_right = 0
        stationary_to_left = 0
        count = 0

        for car in directions:
            if car == "R":
                moving_right += 1
            elif car == "L":
                if moving_right > 0:
                    count += 1 + moving_right
                    moving_right = 0
                    stationary_to_left = True
                elif stationary_to_left:
                    count += 1
            
            elif car == "S":
                stationary_to_left = True
                count += moving_right
                moving_right = 0

        return count
