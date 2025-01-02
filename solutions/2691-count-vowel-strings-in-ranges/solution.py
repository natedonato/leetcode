class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a","e","i","o", "u"}
        prefix = [0]
        p = 0
        
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                p += 1
                
            prefix.append(p)
        
        output = []

        for query in queries:
            output.append(prefix[query[1] + 1] - prefix[query[0]])
        
        return output
