class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]

        def find(n):
            print("")
            while parents[n] != n:
                n = parents[n]
            return n
        
        def merge(a, b):
            p1 = find(a)
            p2 = find(b)
            if p1 != p2:
                parents[b] = p1
                parents[a] = p1
                parents[p2] = p1

        for i in range(len(isConnected)):
            for j in range(i, len(isConnected)):
                if isConnected[i][j] == 1:
                    merge(i, j)

        count = 0
        for i, p in enumerate(parents):
            if i == p:
                count += 1

        return count
