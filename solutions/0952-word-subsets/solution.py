class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_counts = [0] * 26

        for word in words2:
            counts = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                counts[idx] += 1
                if counts[idx] > max_counts[idx]:
                    max_counts[idx] = counts[idx]
        out = []

        for word in words1:
            counts = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                counts[idx] += 1
            valid = True

            for i in range(0,26):
                if counts[i] < max_counts[i]:
                    valid = False
                    break

            if valid:
                out.append(word)

        return out
