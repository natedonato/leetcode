class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        code = {" ": " "}
        index = 0

        for c in key:
            if c not in code:
                code[c] = chr(ord("a") + index)
                index += 1

        out = [code[c] for c in message]

        return "".join(out)
