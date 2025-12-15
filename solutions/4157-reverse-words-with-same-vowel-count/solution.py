class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        first = s[0]
        words = s[1:]
        target = self.countVowels(first)
        out = [first]
        for word in words:
            if self.countVowels(word) == target:
                out.append(word[::-1])
            else:
                out.append(word)

        return " ".join(out)


    def countVowels(self, s):
        count = 0
        for c in s:
            if c in "aeiou":
                count += 1

        return count

