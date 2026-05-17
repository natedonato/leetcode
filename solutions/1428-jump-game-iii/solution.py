class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set([start])
        q = deque([start])
        l = len(arr)

        while q:
            i = q.popleft()
            val = arr[i]
            if val == 0:
                return True

            jumps = [i - val, i + val]
            for j in jumps:
                if j >= 0 and j < l and j not in seen:
                    seen.add(j)
                    q.append(j)
            


        return False
