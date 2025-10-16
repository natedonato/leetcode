class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        c = Counter(map(lambda e: e % value, nums))
        offset = 0
        min_c = math.inf

        for i in range(value):
            count = c[i]

            if count == 0:
                return i
                
            if count < min_c:
                offset = i
                min_c = count

        return min_c * value + offset
