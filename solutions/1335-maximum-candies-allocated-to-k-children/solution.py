class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 0
        r = max(candies) + 1

        while(l < r):
            mid = l + ((r - l) // 2)

            if not self.isValidNumCandies(mid, candies, k):
                r = mid
            else:
                l = mid + 1


        return l - 1
        
        # L is minimum index satisfying condition






    def isValidNumCandies(self, num, candies, k):
        num_satisfied_kids = 0
        if(num == 0):
            return True
        for pile in candies:
            num_satisfied_kids += pile // num
        
        return num_satisfied_kids >= k

    
        # binary search to find the ideal number of candies per kid
        #  
        # isValidNumCandies(num):
        #   test if we can make enough piles for every kid of NUM candies
        #   iterate through the candies
        #    from a pile of candies, we can satisfy candy // num kids    

        # find the max num of candies
        #   bsearch over the number of candies to find the max
        #   0 -> max
            # return the largest that is valid

