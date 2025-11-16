class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        out = [0,0]

        for i in range(1, len(nums)+1):
            if i not in c:
                out[1] = i
            elif c[i] == 2:
                out[0] = i

        return out
