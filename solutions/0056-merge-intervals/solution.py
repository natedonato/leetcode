class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        output = []

        for i in range(1, len(intervals)):
            next_interval = intervals[i]
            next_start, next_end = next_interval

            if next_start <= current_end:
                current_end = max(current_end, next_end)
            else:
                output.append([current_start, current_end])
                current_start = next_start
                current_end = next_end

        output.append([current_start, current_end])

        return output
