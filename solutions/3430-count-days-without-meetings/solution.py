class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()



        current_day = 1
        count = 0
        for meeting in meetings:
            if current_day < meeting[0]:
                count += meeting[0] - current_day

            if current_day <= meeting[1]:
                current_day = meeting[1] + 1

        if current_day < days + 1:
            count += days - current_day + 1

        return count
