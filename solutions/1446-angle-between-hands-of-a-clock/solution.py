class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour += minutes / 60

        hour *= 30
        minutes *= 6

        diff = abs(hour - minutes)
        return min(diff, 360 - diff)
