class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        
        idx = bisect.bisect_right(letters, target)
        return letters[idx]
