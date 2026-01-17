class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(bottomLeft) - 1):
            for j in range(i+1, len(bottomLeft)):
                [x_min1, y_min1] = bottomLeft[i]
                [x_max1, y_max1] = topRight[i]

                [x_min2, y_min2] = bottomLeft[j]
                [x_max2, y_max2] = topRight[j]

                x_min = max(x_min1, x_min2)
                x_max = min(x_max1, x_max2)

                y_min = max(y_min1, y_min2)
                y_max = min(y_max1, y_max2)

                if x_max > x_min and y_max > y_min:
                    squarea = min(x_max - x_min, y_max - y_min) ** 2
                    max_area = max(squarea, max_area)

        return max_area
