class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        points.sort(key = lambda p: (p[0], -p[1]))
        n = len(points)
        count = 0

        for i in range(n):
            point1 = points[i]
            upper_y = point1[1]
            prev_y = -math.inf

            for j in range(i+1, n):
                point2 = points[j]
                lower_y = point2[1]

                if lower_y <= upper_y and lower_y > prev_y:
                    count += 1
                    prev_y = lower_y

        
        return count
