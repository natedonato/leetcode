class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = []
        sum = 0
        for i in range(1, n):
            out.append(i)
            sum += i
        out.append(0-sum)
        return out
