class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        @cache
        def dp(i):
            jumps = []
            for j in range(1,d + 1):
                next_i = i + j
                if next_i == len(arr) or arr[next_i] >= arr[i]:
                    break
                jumps.append(dp(next_i))
                
            for j in range(1,d + 1):
                next_i = i - j
                if next_i < 0 or arr[next_i] >= arr[i]:
                    break
                jumps.append(dp(next_i))

            return 1 + max(jumps, default = 0)

        max_jumps = 0
        for i in range(len(arr)):
            max_jumps = max(max_jumps, dp(i))

        return max_jumps
