class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s=sentence.split(" ")
        print(s)
        out = []
        for i in range(len(s)):
            w = s[i]
            if w[0] not in "aeiouAEIOU":
                w = w[1:]+w[0]
            w += "ma" + ((i+1) * "a")
            out.append(w)

        return " ".join(out)
            
