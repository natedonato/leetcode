class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        target_counts = self.makeCharCount(s)
        stretchy_count = 0

        for word in words:
            word_counts = self.makeCharCount(word)
            isStretchy = True

            if len(word_counts) != len(target_counts):
                continue

            for i in range(len(word_counts)):
                word_count = word_counts[i]
                target_count = target_counts[i]

                if word_count[0] != target_count[0]:
                    isStretchy = False
                    break
                
                if word_count[1] > target_count[1]:
                    isStretchy = False
                    break
                
                if word_count[1] < target_count[1] and target_count[1] < 3:
                    isStretchy = False
                    break

            if isStretchy:
                stretchy_count += 1
        
        return stretchy_count

    def makeCharCount(self, string):
        char_counts = []
        prev = None
        current_count = 0

        for char in string:
            if char == prev:
                current_count += 1
            else:
                if prev != None:
                    char_counts.append((prev, current_count))
                prev = char
                current_count = 1

        char_counts.append((prev, current_count))
        return char_counts

