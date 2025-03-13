class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l = 0
        r = len(queries)

        while(l < r):
            mid = (r - l) // 2 + l

            if(self.testK(mid, queries, nums) == True):
                r = mid
            else:
                l = mid + 1

        if(l < len(queries)):
            return l
        else:
            if(self.testK(l,queries, nums)):
                return l
            else:
                return -1

    def testK(self, k, queries, nums):
        diff_array = [0] * (len(nums) + 1)
        for i in range(0,k):
            query = queries[i]
            diff_array[query[0]] += query[2]
            diff_array[query[1] + 1] -= query[2]
        
        running_sum = 0
        for i in range(len(nums)):
            running_sum += diff_array[i]
            if nums[i] > running_sum:
                return False

        return True

