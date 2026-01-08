class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        self.nums1= nums1
        self.nums2 = nums2

        return self.dp(0,0)

    
    @cache
    def dp(self, i, j):
        possibilities = []

        # base case
        if i == len(self.nums1) or j == len(self.nums2):
            return -math.inf

        # take the dots we are at right now
        dot = self.nums1[i] * self.nums2[j]

        possibilities.append(dot)
        possibilities.append(dot + self.dp(i+1, j+1))
        # pass on i
        possibilities.append(self.dp(i+1,j))

        # pass on j
        possibilities.append(self.dp(i,j+1))

        # return maximum
        return max(possibilities)
