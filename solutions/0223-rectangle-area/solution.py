class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if ax1 > bx1:
            ax1, bx1 = bx1, ax1
            ay1, by1 = by1, ay1
            ax2, bx2 = bx2, ax2
            ay2, by2 = by2, ay2

        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        
        if bx1 >= ax2 or by1 >= ay2 or by2 <= ay1:
            return (area2 + area1)

        minx = max(bx1, ax1)
        maxx = min(ax2, bx2)
        miny = max(by1, ay1)
        maxy = min(by2, ay2)
        overlap_area = (maxx - minx) * (maxy-miny)

        return area2 + area1 - overlap_area
