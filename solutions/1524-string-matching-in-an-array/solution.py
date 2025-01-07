class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set()
        for word in words:
            for word2 in words:
                if word in word2 and word != word2:
                    output.add(word)
                    
        return list(output)
