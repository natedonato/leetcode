class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        min_dist = math.inf
        last_seen = {}

        for i in reversed(range(len(nums))):
            num = nums[i]
            r_num = self.reverse(num)

            if r_num in last_seen:
                min_dist = min(min_dist, last_seen[r_num] - i)
            
            last_seen[num] = i

        if min_dist == math.inf:
            return -1

        return min_dist
        

    def reverse(self, num):
        n = list(str(num))
        n.reverse()
        return int("".join(n))


