class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        s = sum(nums)

        score = sum([n * i for i,n in enumerate(nums)])
        best = score

        for i in range(len(nums)):
            score -= s
            score += nums[i] * len(nums)
            best = max(best, score)

        return best
        
