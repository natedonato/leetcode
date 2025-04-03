class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_to_right = [0] * n
        max_to_right[-1] = -math.inf

        for i in reversed(range(n-1)):
            max_to_right[i] = max(max_to_right[i+1], nums[i+1])
        
        left_max = nums[0]
        score = 0

        for i in range(1,n-1):
            mid = nums[i]
            score = max(score, (left_max - mid) * max_to_right[i])
            left_max = max(left_max, mid)

        return score

