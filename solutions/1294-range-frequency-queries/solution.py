class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.map = {}
        for idx, el in enumerate(arr):
            if el not in self.map:
                self.map[el] = []
            self.map[el].append(idx)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.map:
            return 0

        left_idx = bisect.bisect_left(self.map[value], left)
        right_idx = bisect.bisect_right(self.map[value],right)

        return right_idx - left_idx


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

