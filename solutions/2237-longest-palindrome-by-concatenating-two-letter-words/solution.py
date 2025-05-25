class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)
        extra_middle = 0
        total = 0

        for item, count in counts.items():

            if item[0] == item[1]:
                if count % 2 == 1:
                    if extra_middle == 0: 
                        extra_middle = 2
                    total += (count - 1) * 2
                else:
                    total += count * 2
            else:
                back = item[::-1]
                if back in counts:
                    total += min(count, counts[back]) * 2

        return total + extra_middle
