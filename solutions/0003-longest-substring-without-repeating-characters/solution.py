class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        characters = set()
        
        while right < len(s):
            next_char = s[right]

            while next_char in characters:
                characters.remove(s[left])
                left += 1

            characters.add(next_char)
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length
