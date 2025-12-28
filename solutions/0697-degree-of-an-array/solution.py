class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        m = {}

        for i, num in enumerate(nums):
            if num not in m:
                m[num] = {"start": i, "end": i, "count": 1}
            else:
                m[num]["end"] = i
                m[num]["count"] += 1

        max_degree = 0
        min_length = math.inf

        for item in m.values():
            start = item["start"]
            end = item["end"]
            count = item["count"]
            if count > max_degree:
                max_degree = count
                min_length = end - start + 1
            elif count == max_degree:
                min_length = min(min_length, end - start + 1)

        return min_length
