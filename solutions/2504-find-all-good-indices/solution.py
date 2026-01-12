class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        non_increasing = [0] * len(nums)
        non_decreasing = [0] * len(nums)

        non_increasing[0] = 1
        non_decreasing[-1] = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                non_increasing[i] = 1
            else:
                non_increasing[i] = non_increasing[i-1] + 1

        for i in reversed(range(0, len(nums) - 1)):
            if nums[i] > nums[i+1]:
                non_decreasing[i] = 1
            else:
                non_decreasing[i] = non_decreasing[i+1] + 1

        output = []

        for i in range(0+k, len(nums)-k):
            if non_increasing[i-1] >= k and non_decreasing[i+1] >= k:
                output.append(i)

        return output
