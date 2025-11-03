class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        out = []

        for (el, count) in c.items():
            for i in range(count):
                if len(out) <= i:
                    out.append([])

                out[i].append(el)

        return out
