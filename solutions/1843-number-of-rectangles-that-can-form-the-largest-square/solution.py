class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_side_length = 0
        count = 0

        for rect in rectangles:
            side = min(rect[0],rect[1])
            if side > max_side_length:
                max_side_length = side
                count = 0
            
            if side == max_side_length:
                count += 1

        return count
