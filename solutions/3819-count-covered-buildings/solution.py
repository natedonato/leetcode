class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xs = {}
        ys = {}
        for building in buildings:
            [x,y] = building
            if x not in xs:
                xs[x] = [y]
            else:
                xs[x].append(y)

            if y not in ys:
                ys[y] = [x]
            else:
                ys[y].append(x)

        for x in xs.values():
            x.sort()
        for y in ys.values():
            y.sort()
        
        count = 0
        for building in buildings:
            [x,y] = building

            row = xs[x]
            col = ys[y]

            if y != row[0] and y != row[-1] and x != col[0] and x != col[-1]:
                count += 1

        return count
