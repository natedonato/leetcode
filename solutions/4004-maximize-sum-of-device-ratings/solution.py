class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        dumps = []
        mins = []
        for row in units:
            row.sort()
            
            if len(row) == 1:
                mins.append(row[0])
            else:
                dumps.append(row[0])
                mins.append(row[1])


        mins.sort()
        if len(dumps) == 0:
            return sum(mins)
        return min(dumps) + sum(mins[1:])
        
