class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        out = []

        for i in range(0,len(s),k):
            next_chunk = s[i:i+k]
            while(len(next_chunk) < k):
                next_chunk += fill
            out.append(next_chunk)

        return out
