class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        depth = 0
        g = {}

        for edge in edges:
            p1, p2 = edge
            if p1 not in g:
                g[p1] = []
            if p2 not in g:
                g[p2] = []

            g[p1].append(p2)
            g[p2].append(p1)

        q = deque([1])
        seen = {1}
        while q:
            depth += 1
            l = len(q)
            for _ in range(l):
                n = q.popleft()
                if n in g:
                    for c in g[n]:
                        if c not in seen:
                            seen.add(c)
                            q.append(c)


        even, odd = 1, 0

        for _ in range(depth - 1):
            even, odd = even + odd, even + odd

        return odd % 1000000007
            
