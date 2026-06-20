class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n-1])
    
        
        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            prev_idx, prev_height = restrictions[i-1]

            dist = idx - prev_idx
            restrictions[i][1] = min(prev_height + dist, height)

        for i in reversed(range(0, len(restrictions) - 1)):
            idx, height = restrictions[i]
            post_idx, post_height = restrictions[i+1]

            dist = post_idx - idx
            restrictions[i][1] = min(post_height + dist, height)

        max_height = 0

        for i in range(1, len(restrictions)):
            idx, height = restrictions[i]
            prev_idx, prev_height = restrictions[i-1]
            curr_height = (idx - prev_idx + height + prev_height) // 2

            max_height = max(max_height, curr_height)

        return max_height
