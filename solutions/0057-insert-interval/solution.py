class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        inserted = False

        for i in intervals:
            if i[1] < newInterval[0]:
                out.append(i)
            elif i[0] > newInterval[1]:
                if not inserted:
                    out.append(newInterval)
                    inserted = True
                out.append(i)
            else:
                newInterval[0] = min(newInterval[0],i[0])
                newInterval[1] = max(newInterval[1], i[1])

        if not inserted:
            out.append(newInterval)

        return out
