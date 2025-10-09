from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        out = []
        available_drys = SortedList()
        wet_lakes = {}
        for i in range(len(rains)):
            lake = rains[i]

            if lake != 0:
                out.append(-1)
                if lake in wet_lakes:
                    prev_day = wet_lakes[lake]
                    possible_draining_index = available_drys.bisect(wet_lakes[lake])

                    if possible_draining_index >= len(available_drys):
                        return []

                    draining_day = available_drys[possible_draining_index]
                    out[draining_day] = lake

                    available_drys.remove(draining_day)

                wet_lakes[lake] = i
            else:
                available_drys.add(i)
                out.append(1)
        
        return out
