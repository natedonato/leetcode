class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        m = {}
        for i, v in enumerate(s):
            m[v] = i + 1

        return [m[e] for e in arr]
