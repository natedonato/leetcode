class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        self.cuts = cuts
        return self.solve(0, n)

    @cache
    def solve(self, i, j):
        l = bisect.bisect_right(self.cuts, i)
        r = bisect.bisect_left(self.cuts, j)
        
        cuts = self.cuts[l:r]
        
        if len(cuts) == 0:
            return 0
        
        solutions = []

        for cut in cuts:
            left_cost = cut - i
            right_cost = j - cut
            current_cost = self.solve(i, cut) + self.solve(cut, j)
            solutions.append(current_cost)

        return min(solutions) + j - i
