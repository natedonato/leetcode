class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for r in roads:
            a, b, dist = r
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}

            graph[b][a] = dist
            graph[a][b] = dist

        q = deque()
        q.append(1)
        seen = set()
        seen.add(1)

        while q:
            n = q.popleft()
            for n2 in graph[n].keys():
                if n2 not in seen:
                    seen.add(n2)
                    q.append(n2)
            
        m = math.inf

        for n in seen:
            for dist in graph[n].values():
                m = min(m, dist)

        return m
        
