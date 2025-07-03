class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while(len(word) < k):
            next_word = ""
            for char in word:
                if char == "z":
                    next_word += "a"
                else:
                    next_word += chr(ord(char) + 1)
            word += next_word

        return word[k-1]
