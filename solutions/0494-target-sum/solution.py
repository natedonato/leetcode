class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        
        size = len(nums)
        
        @cache
        def dfs(sum: int, i: int):
            subcount = 0
            if(i == size -1):
                if sum + nums[i] == target:
                    subcount += 1
                if sum - nums[i] == target:
                    subcount += 1
            else:
                subcount += dfs(sum - nums[i], i+1)
                subcount += dfs(sum + nums[i], i+1)
            
            return subcount
        
        count += dfs(0,0)
        
        return count
