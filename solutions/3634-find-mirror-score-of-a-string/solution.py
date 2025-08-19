class Solution:
    def calculateScore(self, s: str) -> int:
        stacks = [[] for _ in range(26)]
        score = 0
        
        for i in range(len(s)):
            next_char = s[i]
            mirror_idx = self.getMirrorIdx(next_char)
            if stacks[mirror_idx]:
                prev_idx = stacks[mirror_idx].pop()
                score += i - prev_idx
            else:
                stacks[ord(next_char) - ord('a')].append(i)

        return score

    def getMirrorIdx(self, char):
        offset = ord(char) - ord('a')
        mirror = 25 - offset
        return mirror
