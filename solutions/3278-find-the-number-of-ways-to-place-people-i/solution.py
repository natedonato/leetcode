class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        for p1 in points:
            for p2 in points:
                if p1 == p2:
                    continue
                if p1[0] > p2[0]:
                    continue
                if p1[1] < p2[1]:
                    continue

                overlap = False
                for p3 in points:
                    if p1 == p3 or p2 == p3:
                        continue
                    x1 = p1[0]
                    x2 = p2[0]
                    y1 = p2[1]
                    y2 = p1[1]
                    [x,y] = p3

                    if (x1 <= x and x <= x2) and (y1 <= y and y <= y2):
                        overlap = True
                        break

                if not overlap:
                    count += 1

        return count

