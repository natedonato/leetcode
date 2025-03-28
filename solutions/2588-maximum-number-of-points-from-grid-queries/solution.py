class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        q = []
        current_score = 0        
        sorted_queries = sorted(queries)
        query_idx = 0
        query_length = len(queries)

        query_solutions = {}

        heapq.heappush(q,(grid[0][0],0,0))
        visited = set()
        visited.add((0,0))
        finished = False

        while q:
            current = heapq.heappop(q)
            current_val = current[0]
            current_query = sorted_queries[query_idx]
            # print("\n")
            # print("current query", current_query)
            # print("point:", current[1],current[2])
            # print("current val", current_val)
            # print("score:", current_score)
            
            
            while query_idx < query_length and current_val >= current_query:
                # print("val greater than query")
                query_solutions[current_query] = current_score
                query_idx += 1

                if query_idx >= query_length:
                    finished = True
                    break

                current_query = sorted_queries[query_idx]


            if finished == True:
                break
            
            current_score += 1

            current_point = (current[1],current[2])
            for neighbor in self.neighbors(grid, visited, current_point):
                heapq.heappush(q, (grid[neighbor[0]][neighbor[1]],neighbor[0],neighbor[1]))
        
               
        # print(query_idx)
        while query_idx < query_length:
            current_query = sorted_queries[query_idx]
            query_solutions[current_query] = current_score
            query_idx += 1
 

        # print(query_idx)

        out = [0] * query_length
        # print(current_score)
        # print(query_solutions)

        for i in range(0, query_length):
            query = queries[i]
            if query in query_solutions:
                out[i] = query_solutions[query]

        return out
        


    def neighbors(self, grid, visited, point):
        vects = (
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        )
        l1 = len(grid)
        l2 = len(grid[0])
        output = []

        for vect in vects:
            next_point = (point[0] + vect[0],point[1] + vect[1])
            
            if next_point not in visited and next_point[0] >= 0 and next_point[0] < l1 and next_point[1] >= 0 and next_point[1] < l2:
                output.append(next_point)
                visited.add(next_point)
        
        return output
