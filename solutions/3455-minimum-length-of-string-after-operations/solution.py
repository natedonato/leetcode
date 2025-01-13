class Solution:
    def minimumLength(self, s: str) -> int:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        total = 0
        for count in counts:
            if count > 2:
                if count % 2 == 1:
                    count = 1
                else:
                    count = 2
            
            total += count
            
        return total
        
