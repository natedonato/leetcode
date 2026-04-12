class Solution:
    def minimumDistance(self, word: str) -> int:
        self.coords = self.makeCoords()
        self.word = word

        return self.dp("@","@", 0)

    @cache
    def dp(self, char1, char2, word_idx):
        if word_idx == len(self.word):
            return 0
        
        next_char = self.word[word_idx]

        move_1_cost = self.getDist(next_char, char1)
        move_2_cost = self.getDist(next_char, char2)

        case_1 = move_1_cost + self.dp(next_char, char2, word_idx + 1) 
        case_2 = move_2_cost + self.dp(char1, next_char, word_idx + 1)

        return min(case_1, case_2) 

    def makeCoords(self):
        coords = {}
        letter = 0
        for r in range(5):
            for c in range(6):
                next_letter = chr(ord("A") + letter) 
                coords[next_letter] = [r,c]
                letter += 1
                if letter == 26:
                    break
        
        return coords
    
    def getDist(self, char1, char2):
        if char1 == "@" or char2 == "@":
            return 0
        x1, y1 = self.coords[char1]
        x2, y2 = self.coords[char2]

        return abs(x1 - x2) + abs(y1 - y2)
    
