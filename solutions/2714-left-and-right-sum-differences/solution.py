class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum = 0
        rsum = sum(nums)
        out = []
        for n in nums:
            print(lsum, rsum)
            rsum -= n
            out.append(abs(lsum - rsum))
            lsum += n

        return out
