class Solution:
    def makeFancyString(self, s: str) -> str:
        out = []

        for c in s:
            if len(out) >= 2 and c == out[-1] and c == out[-2]:
                continue
            else:
                out.append(c)

        return "".join(out)
