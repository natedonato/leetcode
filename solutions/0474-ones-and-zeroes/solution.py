class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.max = 0
        self.m = m
        self.n = n
        self.strs = list(map(lambda x: (x.count("0"), x.count("1")), strs))
        return self.dp(0, 0, m, n)
    
    @cache
    def dp(self, count, i, current_m, current_n):
        if current_m < 0 or current_n < 0:
            return 0

        if i >= len(self.strs):
            return count
        
        skip = self.dp(count, i+1, current_m, current_n)
        take = self.dp(count + 1, i+1, current_m - self.strs[i][0], current_n - self.strs[i][1])

        return max(skip, take)
