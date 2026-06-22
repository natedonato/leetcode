class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.Counter(text)

        n = math.inf
        
        for char in "ban":
            n = min(n, count[char])

        for char in "lo":
            n = min(n, count[char] // 2)

        return n
