class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        max_height = max([s[1] + s[2] for s in squares])
 
        def getArea(y1):
            area = 0
            for (x,y,l) in squares:
                if y < y1:
                    area += l * (min(y+l, y1) - y)

            return area

        total_area = getArea(max_height)

        l = 0
        r = max_height

        while(r - l) > 1e-6:
            
            mid = (r-l) / 2 + l
            area = getArea(mid)
            if area >= total_area / 2:
                r = mid
            else:
                l = mid
    
        return l
