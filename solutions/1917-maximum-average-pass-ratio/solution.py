class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # priority = amount that average will improve by adding a student

        ace_count = 0
        pq = []

        for c in classes:
            [passes, total] = c
            if passes != total:
                heapq.heappush(pq, [self.potentialGain(passes, total), passes, total])
            else:
                ace_count += 1

        while extraStudents and pq:
            next_class = heapq.heappop(pq)
            next_class[1] += 1
            next_class[2] += 1

            gain = self.potentialGain(next_class[1], next_class[2])
            heapq.heappush(pq, [gain, next_class[1], next_class[2]])
            extraStudents -= 1

        avg = 0

        for c in pq:
            avg += c[1] / c[2]
        
        avg += ace_count
        avg /= len(classes)

        return avg

    def potentialGain(self, passes, total):
        prev_ratio = passes / total
        potential_ratio = (passes + 1) / (total + 1)
        return -(potential_ratio - prev_ratio)

