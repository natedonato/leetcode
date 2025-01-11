class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counts = [0] * 26
        
        for char in s:
            counts[ord(char) - ord("a")] += 1
            
        odds = 0
        for count in counts:
            if count % 2 != 0:
                odds += 1
                
        return odds <= k and k <= len(s)
     
