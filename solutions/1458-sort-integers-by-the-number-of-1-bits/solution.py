class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = [(e.bit_count(), e) for e in arr]
        arr.sort()
        return [e[1] for e in arr]
