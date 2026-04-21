class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        union = [i for i in range(len(source))]

        def find(x):
            while union[x] != x:
                x = find(union[x])
            return x

        def merge(x, y):
            p1 = find(x)
            p2 = find(y)

            union[p2] = p1

        for p in allowedSwaps:
            merge(p[0], p[1])

        print(union)
        s = {}
        
        for i, val in enumerate(source):
            parent = find(i)
            if parent not in s:
                s[parent] = {}

            if val not in s[parent]:
                s[parent][val] = 0

            s[parent][val] += 1

        out = 0
        for i, c in enumerate(target):
            group = find(i)
            if c in s[group]:
                if s[group][c] > 0:
                    s[group][c] -= 1
                else:
                    out += 1
            else:
                out += 1
        return out
        
