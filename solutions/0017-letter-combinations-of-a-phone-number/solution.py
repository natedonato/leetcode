class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz" 
        }
        if(len(digits)) == 0:
            return []

        if(len(digits) == 1):
            return list(mapping[digits])
        
        first = digits[0]
        rest = digits[1::]
        sub = self.letterCombinations(rest)
        out = []

        for c in mapping[first]:
            out += map(lambda e: c + e, sub)

        return out
