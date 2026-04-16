class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prev = {}
        solutions = [math.inf] * len(nums)
        
        for i, n in enumerate(nums):
            prev[n] = i

        for i, n in enumerate(nums):
            if prev[n] == i:
                solutions[i] = -1
            
            idxes = [prev[n], i]
            idxes.sort()

            dist_inner = idxes[1] - idxes[0]
            dist_outer = idxes[0] + len(nums) - idxes[1]

            min_dist = min(dist_inner, dist_outer)

            solutions[idxes[0]] = min(solutions[idxes[0]], min_dist)
            solutions[idxes[1]] = min(solutions[idxes[1]], min_dist)

            prev[n] = i

        out = []

        for q in queries:
            if solutions[q] == math.inf:
                out.append(-1)
            else:
                out.append(solutions[q])
        
        return out
