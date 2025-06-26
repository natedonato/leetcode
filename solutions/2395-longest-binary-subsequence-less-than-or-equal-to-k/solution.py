class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        while int(s, 2) > k:
            s = s.replace("1","0", 1)
            count += 1
        
        return len(s) - count

        
