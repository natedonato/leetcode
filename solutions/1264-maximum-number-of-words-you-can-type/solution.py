class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        s = set(brokenLetters)
        words = text.split(" ")
        
        for word in words:
            valid = True
            for c in word:
                if c in s:
                    valid = False
                    break
            
            count += valid

        return count
