class Solution:
    def minJumps(self, arr: List[int]) -> int:
        m = {}
        for i, n in enumerate(arr):
            if n not in m:
                m[n] = []

            m[n].append(i)

        seen = set([0])
        q = deque([0])
        l = len(arr)
        steps = 0

        while q:
            length = len(q)

            for _ in range(length):
                i = q.popleft()
                val = arr[i]
                if i == l - 1:
                    return steps

                jumps = [i - 1, i + 1]
                if val in m:
                    jumps += m.pop(val)
                for j in jumps:
                    if j >= 0 and j < l and j not in seen:
                        seen.add(j)
                        q.append(j)

            steps += 1
