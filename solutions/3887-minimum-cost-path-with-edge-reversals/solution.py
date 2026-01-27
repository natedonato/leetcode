class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        #{ node: [(child_node, weight), ...]}
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for n1, n2, w in edges:
            graph[n1].append((n2, w))
            graph[n2].append((n1, 2 * w))
        
        # (total_dist, node)
        q = [(0, 0)]
        seen = set()

        while q:
            (dist, node) = heapq.heappop(q)
            if node == n - 1:
                return dist

            if node in seen:
                continue
            seen.add(node)

            for child, weight in graph[node]:
                if child not in seen:
                    heapq.heappush(q, (weight + dist, child))

        return -1
