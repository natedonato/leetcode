class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
       nums.sort()
       out = []

       i = 0
       while i < len(nums):
           a = nums[i]
           b = nums[i + 1]
           c = nums[i + 2]
           if c - a > k:
               return []
           else:
               out.append([a,b,c])
               i += 3
               
       return out
