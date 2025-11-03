class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.strip().split(" ")

        out = []
        out.append("#" + words[0].lower())

        for i in range(1,len(words)):
            if words[i]:
                out.append(words[i][0].upper() + words[i][1:].lower())

        return "".join(out)[:100]
