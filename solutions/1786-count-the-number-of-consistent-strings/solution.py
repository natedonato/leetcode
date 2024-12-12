class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set()
        for char in allowed:
            s.add(char)
            
        count = 0
        
        def consistent(word):
            for char in word:
                if char not in s:
                    return False
                
            return True
        
        for word in words:
            if consistent(word):
                count += 1
            
        return count
