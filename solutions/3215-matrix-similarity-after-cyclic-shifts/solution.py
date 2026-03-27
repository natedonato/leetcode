class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        k %= n

        for i, r in enumerate(mat):
            prev = ",".join(str(c) for c in r)
            for _ in range(k):
                if i % 2 == 0:
                    first = r[0]
                    for index in range(0, len(r)-1):
                        r[index] = r[index + 1]
                    r[-1] = first
                else:
                    last = r[-1]
                    for index in reversed(range(1, len(r))):
                        r[index] = r[index - 1]
                    r[0] = last

            curr = ",".join(str(c) for c in r)
            if prev != curr:
                return False

        return True

