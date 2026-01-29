class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = {}
        for i in range(len(original)):
            p1 = original[i]
            p2 = changed[i]
            w = cost[i]

            if p1 not in graph:
                graph[p1] = []

            graph[p1].append((p2, w))

        cache = {}
        total = 0

        for i in range(len(source)):
            start = source[i]
            end = target[i]
            if (start, end) in cache:
                total += cache[(start,end)]
                continue
            
            seen = set()
            solved = False
            q = [(0, start)]

            while q:
                prev_cost, curr = heapq.heappop(q)
                print(curr, prev_cost)
                if curr == end:
                    total += prev_cost
                    cache[(start,end)] = prev_cost
                    solved = True
                    break

                if curr in seen:
                    continue
                seen.add(curr)

                if curr in graph:
                    children = graph[curr]
                    for child in children:
                        if child not in seen:
                            heapq.heappush(q, (child[1] + prev_cost, child[0]))

            if not solved:
                return -1
        
        return total

