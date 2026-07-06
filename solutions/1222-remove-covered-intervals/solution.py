class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],-x[1]))

        count = 1
        prev = intervals[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[1] > prev[1]:
                count += 1
                prev = curr
        
        return count
