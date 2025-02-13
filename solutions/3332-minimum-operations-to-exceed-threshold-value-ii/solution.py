class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        heapq.heapify(nums)

        while nums[0] < k:
            ops += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            next_num = x * 2 + y
            heapq.heappush(nums, next_num)

        return ops
